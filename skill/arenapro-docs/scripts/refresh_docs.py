#!/usr/bin/env python3
"""ArenaPro 中文文档站刷新工具：重新抓取 https://docs.dao3.fun/arenapro/zh/ 并覆盖 docs-md 中的站点转化件。

依赖：python3 + beautifulsoup4 + markdownify + lxml（pip install beautifulsoup4 markdownify lxml）

用法：
  python3 refresh_docs.py [输出目录]     # 默认为 <本脚本>/../../docs-md（项目库布局）
  python3 refresh_docs.py /tmp/check     # 输出到任意目录做比对

行为说明：
- 页面清单从站点侧边栏自动发现（无需维护链接列表）；
- 只新增/覆盖站点来源页面，不会删除输出目录中的自写文档（如 own/）；
- 空壳页（正文无文字，如 ex.html）自动跳过；
- README.md 索引重新生成，固定包含「文档库入口与说明 → index.md」行，并自动追加 own/ 子目录内自写文档条目。
"""
import html as htmlmod, os, re, sys, tempfile, time, urllib.request
from bs4 import BeautifulSoup, NavigableString

BASE = "https://docs.dao3.fun"
ROOT = "/arenapro/zh/"
SEED = ROOT + "guide/01-introduction/00-toolbox-introduction.html"

try:
    from markdownify import MarkdownConverter
except ImportError:
    print("ERROR: 缺少依赖。请先执行: pip install beautifulsoup4 markdownify lxml")
    sys.exit(2)

def url_to_mdpath(url):
    p = url
    if p.startswith(ROOT):
        p = p[len(ROOT):]
    elif p == ROOT.rstrip("/"):
        p = ""
    else:
        return None
    p = p.split("#")[0].split("?")[0]
    if p == "":
        return "index.md"
    if p.endswith("/"):
        return p + "index.md"
    if p.endswith(".html"):
        return p[:-5] + ".md"
    return p + ".md"

def fetch(url, cache, binary=False):
    fp = os.path.join(cache, url.strip("/").replace("/", "__"))
    if os.path.exists(fp) and os.path.getsize(fp) > 1000:
        return open(fp, "rb").read()
    req = urllib.request.Request(BASE + url, headers={"User-Agent": "Mozilla/5.0 arenapro-docs-refresh"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            open(fp, "wb").write(data)
            return data
        except Exception as e:
            if attempt == 2:
                print("FAIL", url, e, file=sys.stderr)
                return None
            time.sleep(2)

def discover(cache):
    raw = fetch(SEED, cache)
    soup = BeautifulSoup(raw.decode("utf-8", "ignore"), "lxml")
    links = set()
    for a in soup.select("[class*='VPSidebar'] a[href]"):
        h = a["href"]
        if h.startswith(ROOT):
            links.add(h.split("#")[0])
    links.add(ROOT)
    return sorted(links)

class Conv(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags=None):
        return ""

def extract_code_blocks(doc):
    blocks = {}
    for i, div in enumerate(doc.select("div[class*='language-']")):
        m = re.search(r"language-([\w+]+)", " ".join(div.get("class", [])))
        lang = m.group(1) if m else ""
        lines = [l.get_text() for l in div.select("pre span.line")]
        if not lines:
            pre = div.find("pre")
            lines = pre.get_text().split("\n") if pre else []
        blocks["@@CODEBLOCK%03d@@" % i] = (lang, "\n".join(lines).rstrip("\n"))
        div.replace_with(NavigableString("\n@@CODEBLOCK%03d@@\n" % i))
    return blocks

def convert_container(el):
    kind = next((c for c in el.get("class", []) if c in ("tip", "warning", "danger", "info", "details")), None)
    if not kind:
        return
    label_el = el.select_one(".custom-block-title") or el.find("summary")
    label = label_el.get_text(strip=True) if label_el else ""
    if label_el:
        label_el.extract()
    repl = "<blockquote><p><strong>%s</strong></p>%s</blockquote>" % (htmlmod.escape(label), el.decode_contents())
    node = BeautifulSoup(repl, "lxml").blockquote
    node.extract()
    el.replace_with(node)

def clean_content(soup, self_md, md_index, url):
    for sel in ["a.header-anchor", "button.copy", "span.lang", ".VPDocFooter", "aside", ".edit-link", "script", "style"]:
        for el in soup.select(sel):
            el.extract()
    doc = soup.select_one("div.vp-doc") or soup.select_one("main") or soup.body
    blocks = extract_code_blocks(doc)
    for el in list(doc.select("div.tip, div.warning, div.danger, div.info, div.details")):
        try:
            convert_container(el)
        except Exception:
            pass
    for d in list(doc.select("details")):
        d.unwrap()
    for a in doc.find_all("a"):
        href = a.get("href")
        if not href or href.startswith("#"):
            continue
        if not href.startswith("/") and not href.startswith(("http://", "https://", "mailto:", "vscode:")):
            import urllib.parse
            resolved = urllib.parse.urljoin(BASE + url, href)
            href = resolved[len(BASE):] if resolved.startswith(BASE) else resolved
        if href.startswith(ROOT):
            mp = url_to_mdpath(href.split("#")[0])
            frag = re.search(r"#.*", href)
            frag = frag.group(0) if frag else ""
            if mp and mp in md_index:
                a["href"] = os.path.relpath(mp + frag, os.path.dirname(self_md))
            else:
                a["href"] = BASE + href
        elif href.startswith("/"):
            a["href"] = BASE + href
    for img in doc.find_all("img"):
        if img.get("src", "").startswith("/"):
            img["src"] = BASE + img["src"]
    return doc, blocks

def md_fixups(text, blocks):
    def repl(m):
        tok = m.group(1)
        lang, code = blocks[tok] if tok in blocks else ("", "")
        return ("\n```" + lang + "\n" + code + "\n```\n") if tok in blocks else m.group(0)
    text = re.sub(r"(@@CODEBLOCK\d{3}@@)\n?", repl, text)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs-md"))
    os.makedirs(out_dir, exist_ok=True)
    cache = tempfile.mkdtemp(prefix="ap_refresh_")
    links = discover(cache)
    md_index = {url_to_mdpath(u) for u in links} - {None}
    nav, skipped = [], []
    for url in links:
        raw = fetch(url, cache)
        if raw is None:
            continue
        soup = BeautifulSoup(raw.decode("utf-8", "ignore"), "lxml")
        title = re.sub(r"\s*\|\s*ArenaPro Creator\s*$", "", (soup.select_one("title").get_text() if soup.select_one("title") else url)).strip()
        self_md = url_to_mdpath(url)
        if not self_md:
            continue
        doc_el = soup.select_one("div.vp-doc")
        body_text = doc_el.get_text(strip=True) if doc_el else ""
        if title == "ArenaPro Creator" and len(body_text) < 40:
            skipped.append(self_md)
            continue
        if not nav:
            side = soup.select_one("[class*='VPSidebar']")
            if side:
                for item in side.select(".VPSidebarItem"):
                    m = next((re.match(r"level-(\d+)", c) for c in item.get("class", []) if re.match(r"level-(\d+)", c)), None)
                    depth = int(m.group(1)) if m else 0
                    p = item.select_one(":scope > p.text") or item.select_one(":scope > div.collapsible > p.text") or item.find("p", class_="text")
                    if not p:
                        continue
                    label = p.get_text(strip=True)
                    a_ = p.find("a")
                    target = None
                    if a_:
                        mp = url_to_mdpath(a_.get("href", ""))
                        target = mp if mp and mp in md_index else BASE + a_["href"]
                    if label:
                        nav.append((depth, label, target))
        soup2 = BeautifulSoup(raw.decode("utf-8", "ignore"), "lxml")
        doc, blocks = clean_content(soup2, self_md, md_index, url)
        text = md_fixups(Conv(heading_style="ATX", bullets="-").convert_soup(doc), blocks)
        out_path = os.path.join(out_dir, self_md)
        os.makedirs(os.path.dirname(out_path) or out_dir, exist_ok=True)
        open(out_path, "w").write("---\ntitle: %s\nsource: %s%s\n---\n\n%s" % (htmlmod.escape(title), BASE, url, text))
    lines = ["# ArenaPro 中文文档索引", "", "- [文档库入口与说明](index.md)"]
    for depth, label, target in nav:
        lines.append("  " * depth + "- " + ("[%s](%s)" % (label, target) if target else label))
    own = sorted(f for f in os.listdir(os.path.join(out_dir, "own"))) if os.path.isdir(os.path.join(out_dir, "own")) else []
    if own:
        lines += ["", "- 自写文档（own/）"] + ["  - [own/%s](own/%s)" % (f, f) for f in own]
    open(os.path.join(out_dir, "README.md"), "w").write("\n".join(lines) + "\n")
    print("写回站点页: %d；跳过空壳页: %s；README 已再生。" % (len(links) - len(skipped), ", ".join(skipped) or "无"))
    print("注意: 站点首页 index.md 与 ex.html 若为纯 hero/空壳会被跳过，own/ 等自写文件不受影响。")

main()

#!/usr/bin/env python3
"""双源文档刷新工具：1) https://docs.dao3.fun/arenapro/zh/ VitePress 站点 → docs-md 根；2) GitHub box3lab/box3-product-document (Apache-2.0) 的 arena/ 与 api/ → docs-md/arena-official/。均只覆盖站点/镜像来源件，own/ 与 index.md 不触碰。

依赖：python3 + beautifulsoup4 + markdownify + lxml（pip install beautifulsoup4 markdownify lxml）

用法：
  python3 refresh_docs.py [输出目录]        # 双源全量刷新（ArenaPro 插件站 + Arena 产品文档）
  python3 refresh_docs.py --arena-only [目录]  # 只刷新 arena-official（GitHub tarball 源）

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

# ---------- 第二文档源: box3lab/box3-product-document (Apache-2.0) ----------
BPD = "box3lab/box3-product-document"
BPD_BRANCH = "master"
BPD_TARBALL = "https://codeload.github.com/%s/tar.gz/refs/heads/%s" % (BPD, BPD_BRANCH)
BPD_BLOB = "https://github.com/%s/blob/%s/" % (BPD, BPD_BRANCH)

def fetch_bpd_tar(cache):
    import tarfile
    tp = os.path.join(cache, "bpd.tar.gz")
    if not (os.path.exists(tp) and os.path.getsize(tp) > 500000):
        req = urllib.request.Request(BPD_TARBALL, headers={"User-Agent": "Mozilla/5.0 arenapro-docs-refresh"})
        with urllib.request.urlopen(req, timeout=300) as r, open(tp, "wb") as f:
            f.write(r.read())
    return tarfile.open(tp, "r:gz")

def bpd_convert(text, src_rel, mirror_rel, all_mirrors):
    """Arena 产品文档 md 清洗：script/容器/链接。正文文字不改。"""
    import posixpath
    text = re.sub(r"<script setup>.*?</script>\s*", "", text, flags=re.S)
    text = re.sub(r"^:::\s*(tip|warning|danger|info|details).*?$", lambda m: "**[%s]**" % m.group(1), text, flags=re.M)
    text = re.sub(r"^:::\s*$", "---", text, flags=re.M)
    SITE = {"arena": "https://docs.dao3.fun/arena/", "api": "https://docs.dao3.fun/api/", "voxa": "https://docs.dao3.fun/voxa/", "arenapro": "https://docs.dao3.fun/arenapro/zh/"}
    def abs_url(p):
        top = p.strip("/").split("/")[0]
        if top in SITE:
            return SITE[top] + p[len("/" + top):]
        home = "https://docs.dao3.fun/arena/" if src_rel.startswith("arena/") else "https://docs.dao3.fun/api/"
        return home + p.lstrip("/")
    text = re.sub(r"\]\((/[^)\s]*)", lambda m: "](" + abs_url(m.group(1)), text)
    text = re.sub(r'src="(/[^")\s]*)"', lambda m: 'src="%s"' % abs_url(m.group(1)), text)
    def link(m):
        tgt, frag = m.group(1), (m.group(2) or "")
        if tgt.startswith(("http", "#", "/", "mailto:", "vscode:")):
            return m.group(0)
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(src_rel), tgt)).lstrip("/")
        for c in (resolved, resolved + ".md", resolved + "/index.md"):
            if c in all_mirrors:
                rel = posixpath.relpath(all_mirrors[c], posixpath.dirname(mirror_rel))
                return "](%s%s)" % (rel, frag)
        return "](%s%s/%s%s)" % (BPD_BLOB, posixpath.dirname(src_rel), tgt.lstrip("./"), frag)
    text = re.sub(r"\]\(([^)\s]+)(#[^)]*)?\)", link, text)
    return text

def bpd_title(text, rel):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        return re.sub(r"<[^>]+>", "", m.group(1)).strip()
    return posixpath_title_fallback(rel)

def posixpath_title_fallback(rel):
    import posixpath
    b = posixpath.splitext(posixpath.basename(rel))[0]
    return b if b != "index" else rel.split("/")[0]

def refresh_arena_official(out_dir, cache):
    import posixpath
    tar = fetch_bpd_tar(cache)
    members = {}
    prefix = None
    for tm in tar.getmembers():
        if not tm.isfile():
            continue
        name = tm.name
        if prefix is None:
            prefix = name.split("/")[0] + "/"
        if not name.startswith(prefix):
            continue
        rel = name[len(prefix):]
        if (rel.startswith("arena/") or rel.startswith("api/")) and rel.endswith(".md") and "/defineParser/" not in rel and "/.vitepress/" not in rel:
            members[rel] = tar.extractfile(tm).read().decode("utf-8", "ignore")
    mirror_of = {rel: "arena-official/" + (rel[len("arena/"):] if rel.startswith("arena/") else "api/" + rel[len("api/"):]) for rel in members}
    count = 0
    out_base = os.path.dirname(os.path.abspath(__file__))
    for rel, text in sorted(members.items()):
        mirror_rel = mirror_of[rel]
        cleaned = bpd_convert(text, rel, mirror_rel, mirror_of)
        site = "https://docs.dao3.fun/arena/" if rel.startswith("arena/") else "https://docs.dao3.fun/api/"
        header = "---\ntitle: %s\nsource: %s%s\nsite: %s\nlicense: Apache-2.0 (box3lab/box3-product-document)\n---\n\n" % (htmlmod.escape(bpd_title(text, rel)), BPD_BLOB, rel, site)
        out_path = os.path.join(out_dir, mirror_rel)
        os.makedirs(os.path.dirname(out_path) or out_dir, exist_ok=True)
        open(out_path, "w").write(header + cleaned.strip() + "\n")
        count += 1
    readme = """# Arena 官方产品文档（镜像）

来源：仓库 box3lab/box3-product-document（master），Apache-2.0 许可；在线版 https://docs.dao3.fun/arena/ 与 https://docs.dao3.fun/api/ 。

- `arena-official/`（不含 api/ 子目录）＝ 源仓库 arena/ —— Arena 编辑器用户手册（含 SEL 规则、地图集成、编辑器、功能、javascript API 入口等）；
- `arena-official/api/` ＝ 源仓库 api/ —— Arena 编辑器 API 手册（Game*/Client* 平台 API，AI 写码强相关，全量纳入；defineParser 为构建工具、box3api.zip 为二进制，未纳入）；
- 转化由 refresh_docs.py 完成：加 frontmatter（title/source/site/license）、去 script 块、`:::` 容器降级为文中标记、图片与跨页链接改写；正文文字未改动。图片引用官方站绝对 URL，未本地镜像。
"""
    open(os.path.join(out_dir, "arena-official", "README.md"), "w").write(readme)
    return count

def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    arena_only = "--arena-only" in flags
    out_dir = argv[0] if argv else os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs-md"))
    os.makedirs(out_dir, exist_ok=True)
    cache = tempfile.mkdtemp(prefix="ap_refresh_")
    if arena_only:
        n = refresh_arena_official(out_dir, cache)
        print("arena-official 镜像更新: %d 篇（源 %s@%s，Apache-2.0）。README 未动（--arena-only）。" % (n, BPD, BPD_BRANCH))
        return
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
    arena_n = refresh_arena_official(out_dir, cache)
    lines = ["# ArenaPro 中文文档索引", "", "- [文档库入口与说明](index.md)"]
    for depth, label, target in nav:
        lines.append("  " * depth + "- " + ("[%s](%s)" % (label, target) if target else label))
    own = sorted(f for f in os.listdir(os.path.join(out_dir, "own"))) if os.path.isdir(os.path.join(out_dir, "own")) else []
    if own:
        lines += ["", "- 自写文档（own/）"] + ["  - [own/%s](own/%s)" % (f, f) for f in own]
    if os.path.isdir(os.path.join(out_dir, "arena-official")):
        lines += ["", "- Arena 官方产品文档镜像（arena-official/，Apache-2.0）", "  - [镜像说明](arena-official/README.md)"]
    open(os.path.join(out_dir, "README.md"), "w").write("\n".join(lines) + "\n")
    print("写回站点页: %d；arena-official: %d 篇；跳过空壳页: %s；README 已再生。" % (len(links) - len(skipped), arena_n, ", ".join(skipped) or "无"))
    print("注意: 站点首页 index.md 与 ex.html 若为纯 hero/空壳会被跳过，own/ 等自写文件不受影响。")

main()

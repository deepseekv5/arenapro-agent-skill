#!/usr/bin/env python3
"""ArenaPro 中文文档检索工具（仅依赖 Python 标准库）。

用法：
  search.py <关键词> [更多关键词...]      # 多关键词 AND 检索，输出 文件:行号 + 命中行
  search.py --toc                          # 列出全部文档（章节树，含标题）
  search.py --list                         # 列出文档相对路径清单
  search.py --files <关键词> ...           # 只输出命中的文件与命中次数
  search.py --read <相对路径> [--lines 1-80]  # 分页读取某文档

可选 --docs-dir <路径> 覆盖内置文档目录（默认使用 Skill 自带 references/docs）。
输出自动截断，避免污染上下文窗口。
"""
import os, re, sys, argparse

def find_docs_dir(custom=None):
    if custom:
        if os.path.isdir(custom):
            return custom
        print(f"提示: --docs-dir 指向的路径不存在或不是目录（{custom}），已回退到内置文档目录。", file=sys.stderr)
    env = os.environ.get("ARENAPRO_DOCS_DIR")
    if env:
        if os.path.isdir(env):
            return env
        print(f"提示: ARENAPRO_DOCS_DIR 指向的路径不存在或不是目录（{env}），已回退到内置文档目录。", file=sys.stderr)
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, "..", "references", "docs"),
                 os.path.join(here, "..", "..", "docs-md")):
        cand = os.path.normpath(cand)
        if os.path.isdir(cand):
            return cand
    return None

def iter_docs(root):
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if f.endswith(".md"):
                p = os.path.join(dp, f)
                yield os.path.relpath(p, root).replace(os.sep, "/"), p

def meta(path):
    title, source = "", ""
    with open(path, encoding="utf-8") as fh:
        head = fh.read(2048)
    m = re.search(r"^title:\s*(.+)$", head, re.M)
    if m: title = m.group(1).strip()
    m = re.search(r"^source:\s*(\S+)", head, re.M)
    if m: source = m.group(1)
    return title, source

def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("terms", nargs="*")
    ap.add_argument("--docs-dir")
    ap.add_argument("--toc", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--files", action="store_true")
    ap.add_argument("--read")
    ap.add_argument("--lines", default="")
    ap.add_argument("--max", type=int, default=40)
    a = ap.parse_args()

    docs = find_docs_dir(a.docs_dir)
    if not docs:
        print("ERROR: 未找到文档目录。请设置 --docs-dir 或环境变量 ARENAPRO_DOCS_DIR。")
        sys.exit(2)

    if a.toc:
        for rel, p in iter_docs(docs):
            t, _ = meta(p)
            print(f"{rel}\t{t}")
        return

    if a.list:
        for rel, _ in iter_docs(docs):
            print(rel)
        return

    if a.read:
        p = os.path.join(docs, a.read)
        if not os.path.exists(p):
            print(f"ERROR: 文件不存在: {a.read}"); sys.exit(1)
        lines = open(p, encoding="utf-8").read().splitlines()
        rng = (1, len(lines))
        if a.lines:
            m = re.match(r"(\d+)-(\d+)", a.lines)
            if m: rng = (int(m.group(1)), int(m.group(2)))
        out = lines[rng[0]-1:rng[1]]
        print("\n".join(out))
        remaining = len(lines) - rng[1]
        if remaining > 0:
            print(f"[截断] 还有 {remaining} 行，可用 --lines {rng[1]+1}-{min(rng[1]+200, len(lines))} 继续读取。")
        return

    if not a.terms:
        print(__doc__); sys.exit(0)

    terms = [t.lower() for t in a.terms]
    hits, total_files = [], 0
    per_file = {}
    for rel, p in iter_docs(docs):
        file_hits = 0
        try:
            text = open(p, encoding="utf-8").read()
        except Exception:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines, 1):
            low = line.lower()
            if all(t in low for t in terms):
                file_hits += 1
                if len(hits) < a.max:
                    snippet = line.strip()
                    if len(snippet) > 160: snippet = snippet[:160] + "…"
                    hits.append(f"{rel}:{i}: {snippet}")
        if file_hits:
            per_file[rel] = file_hits
            total_files += 1
    if a.files:
        for rel, n in sorted(per_file.items(), key=lambda x: -x[1]):
            t, _ = meta(os.path.join(docs, rel))
            print(f"{rel}\t{n} 处命中\t{t}")
        if not per_file: print("无命中")
        return
    if not hits:
        print(f"AND 检索无命中。各词单独命中文件数：")
        for t in terms:
            c = sum(1 for rel, p in iter_docs(docs) if t in open(p, encoding="utf-8").read().lower())
            print(f"  {t}: {c} 个文件")
        sys.exit(1)
    print("\n".join(hits))
    n_more = sum(per_file.values()) - len(hits)
    print(f"\n[摘要] {total_files} 个文件命中；显示 {len(hits)} 条" + (f"，还有 {n_more} 条被截断（--max 可调）" if n_more > 0 else "") + "。")
    top = sorted(per_file.items(), key=lambda x: -x[1])[:5]
    print("最佳文件：" + ", ".join(f"{r}({n})" for r, n in top))

if __name__ == "__main__":
    main()

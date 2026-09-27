# INSTALL — ArenaPro Docs Skill 最简安装

## 发给 AI 的一句话（复制下面整段，贴给任意有下载与文件能力的 AI agent，即完成安装）

> 请安装 ArenaPro Docs Skill：从 https://github.com/deepseekv5/arenapro-agent-skill 获取仓库（git clone，或直接下载 Release zip：https://github.com/deepseekv5/arenapro-agent-skill/releases/download/v1.0.0/arenapro-docs-skill-v1.0.0.zip ），把其中的 arenapro-docs 目录（含 SKILL.md、scripts/、references/docs/）完整放到你的技能加载目录——Qoder/QoderWake 为项目级 .qoder/skills/arenapro-docs 或用户级 ~/.qoder/skills/arenapro-docs；如你的客户端技能目录不同，请自行定位等价目录后放入。放置完成后重新加载技能（如执行 /skills reload），然后运行 `python3 <技能目录>/scripts/search.py 时间回溯 --files` 自检：能返回带文件名的检索结果即安装成功。安装后请直接告诉用户：现在可以直接提问 ArenaPro（神岛）开发问题，回答会自带文档出处。

不需要用户具备命令行能力，不依赖特定客户端——任何能下载文件并写入目录的 agent 都能按上面一段完成。

## 人类分步安装（备用）

### 路径 A：git
```bash
git clone https://github.com/deepseekv5/arenapro-agent-skill.git
cp -r arenapro-agent-skill/skill/arenapro-docs ~/.qoder/skills/   # 或项目级 .qoder/skills/
```

### 路径 B：免 git，直接下 zip
下载上方 Release zip，解压得到 `arenapro-docs/`，整个目录拷入技能目录即可。

## 安装后自检清单
1. 技能目录内存在 `SKILL.md`、`scripts/search.py`、`references/docs/`（89 篇 md）。
2. `python3 scripts/search.py --toc` 能列出文档目录。
3. 关键词检索（如 `HMR`、`npm 包`）返回命中文件与排名。
4. 想让 Skill 跟随最新文档：在项目库内把 `ARENAPRO_DOCS_DIR` 指向 docs-md 目录即可回指，无需重装；文档站更新后运行 `scripts/refresh_docs.py` 刷新。

## 说明
- Skill 与文档同仓库发布：docs-md/ 是内容源，skill/arenapro-docs/ 内置其完整副本（references/docs），自包含离线可用。
- 官网（GitHub Pages）：https://deepseekv5.github.io/arenapro-agent-skill/

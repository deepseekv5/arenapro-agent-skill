# ArenaPro Docs Skill

把 ArenaPro（神岛创作平台）官方中文文档全量整理成结构化 Markdown，打包成一个可安装的 Agent Skill。装进任意 AI 编程助手的技能目录后，Agent 回答 ArenaPro 相关问题时会先检索真实文档、附带出处，写代码时遵守官方 API 与生命周期约定，而不是凭模型记忆编造。

> **免责声明**：本项目是独立的社区作品，与 ArenaPro / Dao3（Box3Lab）官方无隶属关系。所收录文档的版权与最终解释权归原官方文档所有，本仓库仅做格式转化与检索封装，全部文件均在 frontmatter 中保留官方原文出处。

## 快速开始

1. 打开 [INSTALL.md](INSTALL.md)，复制第一段话；
2. 把它贴给你正在使用的 AI agent；
3. agent 会自动下载本仓库、把 `arenapro-docs` 安装进自己的技能目录并完成自检。

装好后直接提问即可，例如：「ArenaPro 组件的生命周期顺序是什么？」「HMR 热更新怎么配置？」「时间回溯系统怎么用？」

## 仓库结构

```
docs-md/                ArenaPro 中文文档的 Markdown 转化件（85 篇 + 索引 + 自写使用指南）
skill/arenapro-docs/    可安装的 Agent Skill
  ├── SKILL.md            触发条件与检索规程
  ├── scripts/search.py   零依赖检索（关键词 AND 排名 / 目录 / 分页读取）
  ├── scripts/refresh_docs.py  文档站更新后的重新拉取脚本
  └── references/docs/    内置文档副本，离线自包含
website/                项目官网（纯静态，GitHub Pages 发布）
INSTALL.md              面向 AI 与人类的安装说明
CHANGELOG.md            更新日志
```

## 在线资源

- 官网：https://deepseekv5.github.io/arenapro-agent-skill/
- 最新 Release（Skill zip 直接下载）：https://github.com/deepseekv5/arenapro-agent-skill/releases
- 原文档站：https://docs.dao3.fun/arenapro/zh/

## 本地使用

检索脚本无依赖，只要有 python3：

```bash
python3 skill/arenapro-docs/scripts/search.py 时间回溯 --files
python3 skill/arenapro-docs/scripts/search.py --toc
```

文档更新后，在 `docs-md` 上运行 `python3 skill/arenapro-docs/scripts/refresh_docs.py` 重新拉取；已安装 Skill 的 agent 通过 `ARENAPRO_DOCS_DIR` 指向最新 `docs-md/` 即可回指，无需重装。

## License

文档内容版权归官方文档站所有（见各文件 frontmatter 的 source 字段）；本仓库自写的脚本、索引与指南部分遵循仓库内 LICENSE 声明。

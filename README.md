# ArenaPro Docs Skill

把 ArenaPro（神岛创作平台）官方中文文档全量整理成结构化 Markdown，打包成一个可安装的 Agent Skill。装进任意 AI 编程助手的技能目录后，Agent 装载后按任务路由自主阅读真实文档、附带出处，写代码时遵守官方 API 与生命周期约定，而不是凭模型记忆编造。

> **免责声明**：本项目是独立的社区作品，与 ArenaPro / Dao3（Box3Lab）官方无隶属关系。所收录文档的版权与最终解释权归原官方文档所有，本仓库仅做格式转化与检索封装，全部文件均在 frontmatter 中保留官方原文出处。

## 快速开始

1. 打开 [INSTALL.md](INSTALL.md)，复制第一段话；
2. 把它贴给你正在使用的 AI agent；
3. agent 会自动下载本仓库、把 `arenapro-docs` 安装进自己的技能目录并完成自检。

装好后直接提问即可，例如：「ArenaPro 组件的生命周期顺序是什么？」「HMR 热更新怎么配置？」「GamePlayerEntity 怎么取玩家位置？」验证安装成功的最快方式：问 agent 组件生命周期顺序，它应去读 lifecycle.md 并答对 onLoad → onEnable → start → update（无需任何脚本）。

## 仓库结构

```
docs-md/                ArenaPro 中文文档（89 篇）+ Arena 官方产品文档镜像（210 篇，Apache-2.0）
skill/arenapro-docs/    可安装的 Agent Skill（任务导向文档路由）
  ├── SKILL.md            核心：开发任务 → 该读哪几篇文档 的路由表 + 目录地图
  ├── references/docs/    内置文档库 300 篇，agent 用自带 glob/grep/read 直读，离线自包含
  ├── references/own/     自写手册：写码检查清单、场景速查、设计手记
  └── scripts/            可选加速器：search.py 字面检索、refresh_docs.py 双源刷新（非必需）
website/                项目官网（纯静态，GitHub Pages 发布）
INSTALL.md              面向 AI 与人类的安装说明
CHANGELOG.md            更新日志
```

## 在线资源

- 官网：https://deepseekv5.github.io/arenapro-agent-skill/
- 最新 Release（Skill zip 直接下载）：https://github.com/deepseekv5/arenapro-agent-skill/releases
- 原文档站：https://docs.dao3.fun/arenapro/zh/

## 本地使用

主路径零工具：所有文档就是 `docs-md/`（或 Skill 内 `references/docs/`）下的 Markdown，agent 或人直接用 glob/grep/read。仓库结构本身即导航：`guide/0X-主题/` 按学习顺序编号、`api/<类名>/` 按类归档、`arena-official/` 为 Arena 产品文档镜像。

可选便利脚本（有 python3 时）：`scripts/search.py` 字面检索加速；文档站更新后跑 `scripts/refresh_docs.py`（`--arena-only` 只刷 Arena 源）重新拉取快照。

## License

文档内容版权归官方文档站所有（见各文件 frontmatter 的 source 字段）；本仓库自写的脚本、索引与指南部分遵循仓库内 LICENSE 声明。

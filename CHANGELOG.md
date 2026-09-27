# 更新日志

遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 格式。

## [未发布]

### 计划中
- 收录 Arena 产品文档（box3-product-document / arena 目录）作为第二文档源
- 文档站 API 章节的纳入评估

## [1.0.0] - 2026-09-27

### 新增
- `docs-md/`：ArenaPro 官方中文文档全量 Markdown 化（85 篇，含组件框架、React UI、调试与热更新、npm 包、发布、权限配置、与引擎差异、MCP 工具、社区章节），每篇 frontmatter 保留官方原文出处；站内相对链接改写为本地 `.md` 链接
- 自写文档两篇：Skill 总览（`docs-md/own/overview.md`）、安装与使用指南（`docs-md/own/installation-and-usage.md`）
- `skill/arenapro-docs/`：可安装 Agent Skill——SKILL.md 触发规程 + 零依赖检索脚本（关键词 AND 排名、目录、分页读取、输出截断）+ 内置文档副本自包含分发；支持 `ARENAPRO_DOCS_DIR` 回指最新 `docs-md/`
- `scripts/refresh_docs.py`：文档站更新后的一键重拉脚本，自写文档与索引登记不受覆盖
- 答题与写码手册（检索降级阶梯、生命周期/包名硬性检查清单、出处引用规范）
- `website/`：项目官网，GitHub Pages 发布；安装板块为「复制这段发给 AI」的免手工安装
- `INSTALL.md`：面向任意 AI agent 的一段式自动安装指令

### 修复
- 修正文档中包名误写（`@arena/*` → 官方实际 `@dao3fun/component`、`@dao3fun/react`）
- 剔除源站遗留的空壳页（`ex`、`package/react` 落地页），索引同步更新

### 安全
- 仓库与站点的 GitHub 链接统一指向有效地址；发布链路不含任何凭据

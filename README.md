# ArenaPro Agent 项目库

> 项目库位置：`/Users/zeroneil/Desktop/dao3agent/`（唯一权威路径，所有 Agent 交付物写在这里）


> AI Agent 请在本文件夹内工作。所有产物写入本目录，不要散落到其他路径。

## 目录约定

| 路径 | 用途 | 负责人 |
| --- | --- | --- |
| `docs-md/` | ArenaPro 中文文档全量 md 化产物（来源 https://docs.dao3.fun/arenapro/zh/ ） | 后端 |
| `skill/` | 接入 ArenaPro 文档的 Agent Skill（基于 docs-md 构建） | 后端 |
| `website/` | ArenaPro AI Agent 官网（静态站，专业风格，避免模板化 AI 味） | 老攸前端 |
| `qa/` | 验收记录与测试报告（本地留档，不随仓库分发） | 测试 |

## 交付标准

1. 文档 md 化：覆盖站点全部章节（Quick Start、Core Workflow、Feature Guides、Project/Build、NPM Packages、Frameworks/API、React UI、Config/Permissions、Community、MCP Tools），保留原文层级与链接关系。
2. Skill：可安装、可被 agent 检索调用，内容完整指向 docs-md。
3. 官网：可直接浏览器打开的静态站点，内容与文档一致，设计克制专业。
4. 全部完成后由总管汇总，向用户交付路径与使用说明。

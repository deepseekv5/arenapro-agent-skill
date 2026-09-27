---
title: arenapro-docs Agent Skill 总览
source: 原创文档（本项目产出，非 docs.dao3.fun 原文）
---

# arenapro-docs Agent Skill 总览

## 这是什么

`arenapro-docs` 是一个基于 ArenaPro 官方中文文档构建的可安装 Agent Skill。它把 https://docs.dao3.fun/arenapro/zh/ 全站 89 篇文档以 Markdown 形式内置在 Skill 包内，让任意支持 Skill 机制的 AI Agent（Qoder CLI / QoderWake 数字员工）在回答 ArenaPro、神岛（Shendao）游戏开发问题时，能够检索官方文档原文并带出处作答，而不是依赖模型的模糊记忆。

Skill 实体位于项目库 `skill/arenapro-docs/`，由三部分组成：

| 组成 | 路径 | 作用 |
| --- | --- | --- |
| 触发与流程说明 | `SKILL.md` | frontmatter 中的 name/description 决定何时启用；正文定义检索工作流与回答准则 |
| 检索工具 | `scripts/search.py` | 零依赖 Python 脚本，提供关键词检索、文件命中排名、目录清单、分页读取四种模式 |
| 文档库 | `references/docs/` | ArenaPro 中文文档全量 md（本 `docs-md/` 的同步副本），每篇带 `title` 与官网 `source` |

## 为什么需要它

ArenaPro 开发有大量专有约定：组件生命周期（onLoad→onEnable→start→update）、`Alt+Q` 完整构建与 HMR 热更新的分工、`@dao3fun/react` 的自定义 XML 标签与钩子、`dao3.cfg` 配置项、与 Arena 引擎的差异点（dialog、voxel、storage 等）。这些内容不在通用模型的训练语料中，直接提问容易得到臆造的 API。本 Skill 将权威文档变成 Agent 的按需上下文，回答可溯源、可核对。

## Agent 接入后能做什么

1. **有据答疑**：API 用法、参数、返回值、快捷键以文档原文为准，无命中时明确告知"文档未覆盖"，不编造。
2. **规范写码**：编写组件、React UI、事件通信代码时先检索对应章节，直接引用文档示例骨架。
3. **带出处回答**：每篇文档 frontmatter 保留官网 URL，答复可附来源链接。
4. **差异提醒**：涉及 Arena/ArenaPro 差异、Debug/Release 构建、权限（storage 授权）等易错点时命中 `difference/`、`authority/` 专章。
5. **全站导航**：`--toc`/`README.md` 提供章节树，支持"某功能在哪章"类定位问题。

## 内容覆盖

与 `docs-md/` 一致，覆盖站点侧边栏全部章节：guide 七章（简介、快速上手、Hello World、开发工作流、最佳实践、进阶主题、发布）、`package/component`（组件指南 + API 参考 + 时间回溯系统）、`package/react`（React UI 指南）、`difference`（Arena 差异）、`authority`（权限）、`dao3Cfg`（配置文件）、`community`（社区）、`mcp`（MCP 工具）。代码块、表格、层级结构与内部链接均在转换时保留并经脚本校验。

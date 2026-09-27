---
title: arenapro-docs Agent Skill 总览
source: 原创文档（本项目产出，非 docs.dao3.fun 原文）
---

# arenapro-docs Agent Skill 总览

## 这是什么

`arenapro-docs` 是一个任务导向的文档 Skill：把 ArenaPro 官方中文文档（docs.dao3.fun/arenapro/zh，89 篇）与 Arena 官方产品文档（GitHub box3lab/box3-product-document，Apache-2.0 镜像，210 篇）整理成结构化 Markdown 内置在包内。SKILL.md 的主体是一张「开发任务 → 该读哪几篇文档」的路由表与目录地图——Agent 装载后用自带的 glob/grep/read 文件能力直接定位并通读相关文档，不依赖任何脚本或外部服务，在任何能读写文件的环境都成立。

Skill 实体位于仓库 `skill/arenapro-docs/`：

| 组成 | 路径 | 作用 |
| --- | --- | --- |
| 任务路由主体 | `SKILL.md` | 触发条件 + 开发场景→文档路由表 + 目录地图与命名规律 + 作答准则 |
| 文档库 | `references/docs/` | 全部 300 篇 md（`docs-md/` 同步副本），每篇 frontmatter 带 title/source 出处 |
| 自写手册 | `references/own/` | 写码检查清单与出处规范（answer-playbook.md）、设计手记（skill-design.md） |
| 可选加速器 | `scripts/` | search.py 字面检索、refresh_docs.py 双源刷新——纯可选，缺 python3 不影响任何功能 |

## 为什么需要它

ArenaPro/Arena 开发有大量专有约定：组件生命周期（onLoad→onEnable→start→update）、`Alt+Q` 完整构建与 HMR 热更新的分工、`@dao3fun/react` 的自定义 XML 标签与钩子、`dao3.cfg` 配置、与 Arena 引擎的差异点、以及 Game*/Client* 平台 API。这些不在通用模型训练语料中，凭记忆作答必然编造 API。本 Skill 把权威原文变成 Agent 的按需上下文：装载即知道自己去哪读，回答可溯源。

## Agent 接入后能做什么

1. **自主定位文档**：在 ArenaPro 项目文件夹开发时，按任务场景直接读对应 md，不需要用户指路、不需要检索工具。
2. **有据答疑**：API、参数、快捷键以读到的原文为准，未覆盖时按「未覆盖协议」明确声明，不编造。
3. **规范写码**：写组件/UI/事件/存档代码前先通读生命周期、事件、权限等护栏章节（路由表指定）。
4. **带出处回答**：frontmatter 保留官方 URL（Arena 镜像另带 license/site 声明）。
5. **双源分工**：插件工具链与 Arena 编辑器/平台 API 的分流规则内置于 SKILL.md。

## 安装与自检

见仓库根 `INSTALL.md`（首段即为可直接复制给任意 agent 的一句话安装指令）。安装自检不需要运行任何脚本：让 agent 复述指定文档要点（例如组件生命周期顺序）即可验证。

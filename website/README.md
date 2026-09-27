# ArenaPro Docs Skill 官网

介绍「基于 ArenaPro 中文文档构建的 Agent Skill」的项目官网（静态站），负责人：老攸前端。仓库 `deepseekv5/arenapro-agent-skill`，Pages 发布自本目录（main 分支 /website）。

## 安装板块口径（收紧终版，2026-09-27）

- 主体=INSTALL.md「发给 AI 的一句话」**逐字全文**（脚本核验与仓库 INSTALL.md 首段 verbatim 一致，含反引号与全部 URL）+ 「复制整段」按钮（innerText 纯文本，clipboard API + execCommand 回退，http 环境可用）。
- 次级内容**折叠保留**（原生 details/summary，无 JS 依赖）：路径 A git / 路径 B zip、四项自检清单、docs-dir 解析优先级，注明 INSTALL.md 为单一事实源。
- 出口按钮三个：INSTALL.md 原文（blob）、Release zip 直链、Release 页。

## 链接策略

- 站内已无任何 `../` 相对链接：own 两篇、社区卡仓库链接全部指向 `https://github.com/deepseekv5/arenapro-agent-skill/...`；页脚含 Pages「在线站点」自链，站内事实链接（repo/4×blob/Release 页/zip/Pages）实测全部 200。

## 验证记录（收紧轮）

- HTML 解析零错误、锚点完整；390px 探针在折叠关闭与展开两态均 `cw=375 / sw=375` 无溢出；references/docs 实测 89 篇与自检文案一致；逐字一致性脚本通过。

## 打开方式

浏览器直接打开 `index.html`，或 `python3 -m http.server 8080` 本地预览。文件：index.html / styles.css / app.js（滚动渐入、移动菜单、复制按钮）。

## 页面板块

1. Hero — 主角为 Skill，配 Agent 会话 mock（检索 + 带出处回答）
2. 01 这个 Skill 是什么 — 全量结构化 / 按需检索 / 答案可溯源
3. 02 给谁用 — 创作者 / AI 编程助手与数字员工 / 团队与工具作者
4. 03 装后能做什么 — 8 项能力，逐项映射 docs-md 真实章节
5. 04 安装与使用 — INSTALL.md 一句话 + 复制按钮 + 详情/zip 出口
6. 05 背景：ArenaPro 是什么 — 产品一句话介绍 + 四步工作流 + 官方文档直达
7. 06 反馈与社区 — Box3Lab 组织页 / QQ 群 / 文档时效 / 项目仓库

## 历史口径存档

- 85 篇官方文档转化件；docs-md 全库共 89 篇 = 85 转化件 + index.md + README.md + own/ 两篇原创。
- 历轮 QA 修复（term 对比度、390px 溢出）记录保留在本地 qa/；390px 溢出源（三步教程终端块）已随板块移除，探针每轮回归。

## 设计说明

- 方向：warm-paper 底色 + 墨色正文 + 深青绿主色 + 陶土橙点缀，编辑式编号章节，规避渐变滥用/玻璃拟态/emoji 堆砌的模板站风格。
- 字体：Space Grotesk（拉丁标题）、IBM Plex Mono（代码与标签）、Noto Sans SC（中文正文），Google Fonts 加载失败时优雅回退，离线可正常浏览。
- 动效仅滚动渐入与状态点呼吸，遵循 `prefers-reduced-motion`。

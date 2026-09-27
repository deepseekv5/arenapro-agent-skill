---
title: ArenaPro 中文文档库（本项目转换件入口）
source: https://docs.dao3.fun/arenapro/zh/
---

# ArenaPro 中文文档库

本目录是 https://docs.dao3.fun/arenapro/zh/ （VitePress 站点）的全量 Markdown 转化件。原站首页为纯 hero 落地页（无正文内容），因此本 `index.md` 为自写的导航说明页，正文入口请看 [README.md](README.md)（与站点侧边栏一致的章节树）。

- 站点转化件：本目录除 `own/`、`index.md` 与 `arena-official/` 外的全部 `.md`，每篇 frontmatter 带官网 `source` 原文链接。
- Arena 官方产品文档镜像：`arena-official/`（210 篇，含 api/；来源 GitHub box3lab/box3-product-document，Apache-2.0，署名声明见该目录 README.md）。
- 自写文档：[own/overview.md](own/overview.md)、[own/installation-and-usage.md](own/installation-and-usage.md)。
- 已知空壳页处理：原站 `ex.html` 与 `package/react.html` 正文为空（前者为站点残留测试页），已不纳入本库，导航由 `README.md` 与 `package/react/reactGuide/` 各页承接。

# 官网

ArenaPro Docs Skill 的项目官网，纯静态站，GitHub Pages 从本目录发布（main 分支 /website）。

## 文件

- `index.html` — 单页站全部内容（Hero、Skill 介绍、能力、安装、ArenaPro 背景、社区）
- `styles.css` — 纸墨风主题样式
- `app.js` — 滚动渐入、移动端菜单、安装指令复制（clipboard API + execCommand 回退）

## 本地预览

直接双击打开 `index.html`，或：

```bash
python3 -m http.server 8080
```

## 维护说明

- 安装板块的指令块与仓库根 [INSTALL.md](../INSTALL.md) 首段保持逐字一致，改 INSTALL.md 时同步这里；
- 站内指向文档的链接一律用仓库 blob 地址（`https://github.com/deepseekv5/arenapro-agent-skill/blob/main/...`），避免 Pages 上出现原始 Markdown 文本；
- 字体走 Google Fonts CDN，无构建依赖。

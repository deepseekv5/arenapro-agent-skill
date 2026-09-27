# Arena 官方产品文档（镜像）

来源：仓库 box3lab/box3-product-document（master），Apache-2.0 许可；在线版 https://docs.dao3.fun/arena/ 与 https://docs.dao3.fun/api/ 。

- `arena-official/`（不含 api/ 子目录）＝ 源仓库 arena/ —— Arena 编辑器用户手册（含 SEL 规则、地图集成、编辑器、功能、javascript API 入口等）；
- `arena-official/api/` ＝ 源仓库 api/ —— Arena 编辑器 API 手册（Game*/Client* 平台 API，AI 写码强相关，全量纳入；defineParser 为构建工具、box3api.zip 为二进制，未纳入）；
- 转化由 refresh_docs.py 完成：加 frontmatter（title/source/site/license）、去 script 块、`:::` 容器降级为文中标记、图片与跨页链接改写；正文文字未改动。图片引用官方站绝对 URL，未本地镜像。

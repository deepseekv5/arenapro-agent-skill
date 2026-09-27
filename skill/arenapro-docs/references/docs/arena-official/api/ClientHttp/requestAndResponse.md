---
title: 请求响应
source: https://github.com/box3lab/box3-product-document/blob/master/api/ClientHttp/requestAndResponse.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 请求响应


## 方法

#### <font id="API" />fetch(<font id="Type">url: string, options?: [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit)</font>)<font id="Type">: Promise‹[Response](https://developer.mozilla.org/en-US/docs/Web/API/Response)›</font>{#fetch}

请求指定网站，获取响应数据

**输入参数**

| **_参数_** | **_必填_** | **_默认值_** | **_类型_** | **_说明_** |
| --- | --- | --- | --- | --- |
| url | 是 | | string | 网址 |
| options |  | | RequestInit | 请求配置项 |

**返回值**


| **类型** | **说明** |
| --- | --- |
| Promise‹Response› | 异步返回响应数据 |

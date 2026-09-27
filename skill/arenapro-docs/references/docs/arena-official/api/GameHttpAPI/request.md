---
title: 外部请求
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameHttpAPI/request.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 外部请求


## 方法

#### <font id="API" />fetch(<font id="Type">url: [URL](https://developer.mozilla.org/zh-CN/docs/Web/API/URL), options?:Partial<[GameHttpFetchRequestOptions](https://github.com/box3lab/box3-product-document/blob/master/api/GameHttpAPI/request#GameHttpFetchRequestOptions)></font>)<font id="Type">: Promise<[GameHttpFetchResponse](https://docs.dao3.fun/api/GameHttpAPI/response)></font>{#fetch}

请求指定网站，获取响应数据

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| url | 是 | | URL | 网址 |
| options | | | Partial‹GameHttpFetchRequestOptions› | 请求配置 |

**返回值**

| **类型** | **说明** |
| --- | --- |
| Promise‹GameHttpFetchResponse› | 异步返回响应数据 |





## 接口

#### <font id="API" />GameHttpFetchRequestOptions{#GameHttpFetchRequestOptions}
请求时的配置。

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| timeout | number | 超时时间（毫秒ms），超过后断开请求 |
| method | 'OPTIONS' &#124; 'GET' &#124; 'HEAD' &#124; 'PUT' &#124; 'POST' &#124; 'DELETE' &#124; 'PATCH' | 请求方式 |
| headers | [GameHttpFetchHeaders](https://github.com/box3lab/box3-product-document/blob/master/api/GameHttpAPI/request#GameHttpFetchHeaders) | 请求头对象 |
| body | string &#124; ArrayBuffer | 请求体 |




---


#### <font id="API" />GameHttpFetchHeaders{#GameHttpFetchHeaders}
请求头配置。

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| [name: string] | string &#124; string[] | 请求头列表 |

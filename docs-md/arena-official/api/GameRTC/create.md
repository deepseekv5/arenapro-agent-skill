---
title: 新建通道
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/create.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 新建通道

## 方法
#### <font id="API" />createChannel(<font id="Type">channelId?:string</font>)<font id="Type">: Promise‹[GameRTCChannel](https://docs.dao3.fun/api/GameRTC/operate)›</font>{#createChannel}
新建一个rtc通道

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| channelId |  |  | string | 自定义通道标识 |


**返回值**

| **类型** | **说明** |
| --- | --- |
| Promise‹GameRTCChannel› | 异步返回rtc对象 |

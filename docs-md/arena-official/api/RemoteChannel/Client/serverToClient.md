---
title: 客户端：服务端-&gt;客户端通讯
source: https://github.com/box3lab/box3-product-document/blob/master/api/RemoteChannel/Client/serverToClient.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 客户端：服务端->客户端通讯

## 方法

#### <font id="API" /><font id="Event" >事件</font>onClientEvent(<font id="Type">handler:(args:any)=>void</font>)<font id="Type">: void</font>{#onClientEvent}

监听`服务端`发来的事件

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                     |
| -------- | -------- | ---------- | -------- | ---------------------------- |
| handler  | 是       |            | function | 服务端通过该事件发送的数据。 |

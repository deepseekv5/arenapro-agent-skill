---
title: S-🔊 游戏跨端通讯
source: https://github.com/box3lab/box3-product-document/blob/master/api/RemoteChannel/Server/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# S-🔊 游戏跨端通讯

**ServerRemoteChannel** 是整个游戏跨端通信的服务端接口，它提供了以下核心功能：

- 服务端消息发送：向指定玩家或全体玩家发送事件消息
- 客户端消息接收：监听并处理来自客户端的事件消息
- 跨端数据传输：支持结构化数据的跨端安全传递

你可以通过全局对象 `remoteChannel` 来使用这些功能。

## 类定义

```typescript
declare const remoteChannel: ServerRemoteChannel;
declare class ServerRemoteChannel {
  //...
}
```

## 方法列表

### 服务端发送

- [`sendClientEvent`](https://docs.dao3.fun/api/RemoteChannel/Server/serverToClient#sendClientEvent) : 向**指定玩家**发送事件消息
- [`broadcastClientEvent`](https://docs.dao3.fun/api/RemoteChannel/Server/serverToClient#broadcastClientEvent) : 向**所有玩家**广播事件消息

### 客户端监听

- [`onServerEvent`](https://docs.dao3.fun/api/RemoteChannel/Server/clientToServer#onServerEvent) : 监听并处理来自客户端的事件消息

---
title: S-🗣️ 游戏实时语音通讯
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# S-🗣️ 游戏实时语音通讯

**GameRTC** 是游戏中的实时语音通讯系统，提供以下核心功能：

- 语音通道：创建和管理语音通讯频道
- 权限控制：管理玩家的麦克风权限
- 成员管理：添加或移除通道成员
- 音量控制：调节玩家语音音量

你可以通过全局对象 `rtc` 来使用这些功能。

## 类定义

```typescript
declare const rtc: GameRTC;
declare class GameRTC {
  //...
}
```

## 方法列表

### 通道管理

- [`createChannel`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/create#createChannel) : 创建一个新的语音通道
- [`destroy`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#destroy) : 销毁指定的语音通道
- [`getPlayers`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#getPlayers) : 获取通道内的所有玩家列表

### 权限管理

- [`getMicrophonePermission`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#getMicrophonePermission) : 请求获取指定玩家的麦克风权限
- [`publishMicrophone`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#publishMicrophone) : 允许玩家在通道内开启麦克风
- [`unpublish`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#unpublish) : 关闭玩家在通道内的麦克风

### 成员管理

- [`add`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#add) : 将玩家添加到语音通道
- [`remove`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#remove) : 将玩家从语音通道中移除

### 音量控制

- [`getVolume`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#getVolume) : 获取指定玩家在通道内的音量
- [`setVolume`](https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate#setVolume) : 设置指定玩家在通道内的音量

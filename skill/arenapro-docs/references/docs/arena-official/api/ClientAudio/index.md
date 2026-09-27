---
title: 客户端音频
source: https://github.com/box3lab/box3-product-document/blob/master/api/ClientAudio/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 客户端音频

> Audio 是继承自 [UiEvent](https://docs.dao3.fun/api/ClientUI/UiEvent) 类

客户端音频播放不受引擎内下水等声音变化的影响，但是会受玩家客户端整体音量控制（主音量）

## 构造函数

#### <font id="API" />Audio(<font id="Type">src:string</font>)<font id="Type">: Audio</font>

实例化一个客户端音频对象

**输入参数**

| **_参数_** | **_必填_** | **_默认值_** | **_类型_** | **_说明_** |
| ---------- | ---------- | ------------ | ---------- | ---------- |
| src        | 是         |              | string     | 音频路径   |

```javascript
let url =
  "https://static.dao3.fun/block/QmSkEpcxqFYvZNwZg2EwzTz7y9XNxQnChZ18CDCM8Q8uvE";

const audio = new Audio(url);
```

## 属性

#### <font id="API" />src<font id="Type">: string</font>{#src}

音频路径，目前仅支持白名单内的 URL，不支持项目内音频路径。

技巧：项目内的音频，请复制音频`Hash`，然后拼接在 `https://static.dao3.fun/block/{Hash}`

#### <font id="API" />volume<font id="Type">: number</font>{#volume}

> 范围：0-1

音频播放音量，但最终音量受玩家客户端整体音量控制。

#### <font id="API" />error<font id="Type">: [MediaError](mediaError.md) | null</font>{#error}

音频播放错误码

## 方法

#### <font id="API" />play()<font id="Type">: Promise‹void›</font>{#play}

播放音频

#### <font id="API" />pause()<font id="Type">: void</font>{#pause}

暂停音频

#### <font id="API" />load()<font id="Type">: void</font>{#load}

预加载音频

## 事件

#### <font id="API" />loadeddata<font id="Type">: [UiEvent](https://docs.dao3.fun/api/ClientUI/UiEvent)‹Audio›</font>

音频加载完成事件

#### <font id="API" />ended<font id="Type">: [UiEvent](https://docs.dao3.fun/api/ClientUI/UiEvent)‹Audio›</font>

音频播放结束事件

#### <font id="API" />error<font id="Type">: [UiEvent](https://docs.dao3.fun/api/ClientUI/UiEvent)‹Audio›</font>

音频播放错误事件

```javascript
let url =
  "https://static.dao3.fun/block/QmSkEpcxqFYvZNwZg2EwzTz7y9XNxQnChZ18CDCM8Q8uvE";

const audio = new Audio(url);

//当监听到音频加载完成时触发
audio.add("loadeddata", (e) => {
  //xxx
});

//当监听到音频播放结束时触发
audio.add("ended", (e) => {
  //xxx
});

//当监听到音频发送错误时触发
audio.add("error", (e) => {
  //xxx
});
```

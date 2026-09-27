---
title: S-音乐对象
source: https://github.com/box3lab/box3-product-document/blob/master/api/Sound/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# S-音乐对象

**[info]**
**Sound**，作为 `sound()` 方法的统一返回类型，支持后续的音乐操作。
---
## 方法

#### <font id="API" />setCurrentTime(<font id="Type">currentTime:number</font>)<font id="Type">: void</font>

设置该音乐播放的时间点

**输入参数**

| **参数**    | **必填** | **默认值** | **类型** | **说明**       |
| ----------- | -------- | ---------- | -------- | -------------- |
| currentTime | 是       |            | number   | 设定特定时间点 |

#### <font id="API" />resume(<font id="Type">currentTime?:number</font>)<font id="Type">: void</font>

继续该音乐播放

**输入参数**

| **参数**    | **必填** | **默认值** | **类型** | **说明**             |
| ----------- | -------- | ---------- | -------- | -------------------- |
| currentTime | 否       |            | number   | 从特定时间点继续播放 |

#### <font id="API" />pause()<font id="Type">: void</font>

暂停该音乐的播放

#### <font id="API" />stop()<font id="Type">: void</font>

终止该音乐的播放

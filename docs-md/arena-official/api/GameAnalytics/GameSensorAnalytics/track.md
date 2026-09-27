---
title: 神策埋点
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameAnalytics/GameSensorAnalytics/track.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 神策埋点

```js
const sa = analytics.sensor;
world.onPlayerJoin(({ entity }) => {
  console.log(entity.player.userId);
  // 初始化神策配置
  sa.init("https://shence-data.XXX.cn/sa?project=XXX&token=XXX");
  // 追踪一个测试事件
  sa.track(entity.player.userId, "test", {
    n: 3,
    s: "string",
    b: true,
    d: Date.now(),
  });
});
```

## 方法

#### <font id="API" />init(<font id="Type">url:string,timeout?:number</font>)<font id="Type">: void</font>{#init}

初始化神策埋点配置方法

用于设置数据接收地址和超时时间

注意: 以最后一次执行的配置为准

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| url      | 是       |            | string   | 数据接收地址，神策服务器的 URL |
| timeout  |          | 30         | number   | 请求超时时间                   |

#### <font id="API" />track(<font id="Type">distinctId:string,eventName:string,properties?:Record‹string, string | number | boolean›</font>)<font id="Type">: void</font>{#track}

追踪数据事件方法

用于记录用户行为和自定义事件

**输入参数**

| **参数**   | **必填** | **默认值** | **类型**                                            | **说明**                                                 |
| ---------- | -------- | ---------- | --------------------------------------------------- | -------------------------------------------------------- |
| distinctId | 是       |            | string                                              | 追踪数据事件方法，用于记录用户行为和自定义事件           |
| eventName  | 是       |            | string                                              | 用户唯一标识，通常是平台用户 ID(GamePlayerEntity.userId) |
| properties |          | {}         | Record‹string, string &#124; number &#124; boolean› | 事件属性(会被 JSON.stringify 序列化)                     |

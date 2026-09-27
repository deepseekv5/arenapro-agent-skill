---
title: 动作控制器
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameMotionController/controller.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 动作控制器
```javascript
const entity = world.querySelector('#npc')
const entityMotionControl = entity.motion; // GameMotionController
const motion = entityMotionControl.loadByName('hello'); // GameMotionHandler 'hello'指代'npc'实体上的其中一个motion动作名称
motion.onFinish(() => {
  console.log('Motion End');
});
motion.play()

```

## 方法

#### <font id="API" />loadByName(<font id="Type">configs:string | [GameMotionConfig](https://github.com/box3lab/box3-product-document/blob/master/api/GameMotionController/controller#GameMotionConfig)[] | [GameMotionClipConfig](https://github.com/box3lab/box3-product-document/blob/master/api/GameMotionController/controller#GameMotionClipConfig)</font>)<font id="Type">: [GameMotionHandler](https://docs.dao3.fun/api/GameMotionController/handler)</font>{#loadByName}

加载特定动作或动作序列，并返回对应的动作对象  

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| configs | 是 | | string &#124; GameMotionConfig[] &#124; GameMotionClipConfig | 动作名称或配置 |


---


#### <font id="API" />pause()<font id="Type">:  void</font>{#pause}
暂停实体上的动作播放  


---


#### <font id="API" />resume()<font id="Type">:  void</font>{#resume}
恢复实体上的动作播放  


---


#### <font id="API" />setDefaultMotionByName(<font id="Type">motionName:undefined | string</font>)<font id="Type">:  void</font>{#setDefaultMotionByName}
设置默认动作

- 没有其他动作在播放的情况下，默认动作会在游戏运行时自动循环播放
- 调用此函数时，如当前处于默认动作执行状态，则将打断旧默认动作，播放新的默认动作
- 动作名不存在时，此方法不产生任何效果，并抛出包含实体、模型与动作信息的错误

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| motionName |  | | undefined &#124; string | 动作名称 |

```javascript
const entity = world.querySelector('#npc')
entity.motion.setDefaultMotionByName('FirstMotion');
entity.motion.setDefaultMotionByName(''); // 报错，不存在对应动作
entity.motion.setDefaultMotionByName(); // 设置默认动作为空，即不播放默认动作
```


## 接口

#### <font id="API" />GameMotionConfig{#GameMotionConfig}
动作配置

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| iterations | number | 输入Infinity就是无限循环，此时会覆盖掉默认动作，能cancel或者播放新的动作覆盖。可选项，默认 1 次 |
|  name | string | 动作名字 |


---


#### <font id="API" />GameMotionClipConfig{#GameMotionClipConfig}
动作序列配置

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| iterations | number | 输入Infinity就是无限循环，此时会覆盖掉默认动作，能cancel或者播放新的动作覆盖。可选项，默认 1 次 |
| motions | (string &#124; [GameMotionConfig](https://github.com/box3lab/box3-product-document/blob/master/api/GameMotionController/controller#GameMotionConfig))[]   | 可填写指定动作名或motion动作配置 |

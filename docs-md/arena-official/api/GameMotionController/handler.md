---
title: 动作处理器
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameMotionController/handler.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 动作处理器

**[info]**
**GameMotionHandler**，作为`loadByName()`方法的统一返回类型，支持后续的动作操作。 
---
## 属性

#### <font id="API" /><font id="ReadOnly">只读</font>target<font id="Type">: [GameEntity](https://docs.dao3.fun/api/GameEntity/) </font>{#target}


得到当前entity对象



## 方法

#### <font id="API" />play()<font id="Type">:  void</font>{#play}
播放当前实体动作   

- 会打断当前动作，开始对应动作/序列动作的播放
- 当配置中包含的动作播放结束时，触发 `onFinish` 事件 


---


#### <font id="API" />cancel()<font id="Type">:  void</font>{#cancel}
中途打断此动作播放，并触发 `onFinish` 事件  


---


#### <font id="API" /><font id="Event">事件</font>onFinish(<font id="Type">handler:(event:[GameMotionEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameMotionController/handler#GameMotionEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onFinish}
响应结束状态的监听函数 

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | 是 | | function | 监听到实体动作结束时的处理函数 |




## 接口

#### <font id="API" />GameMotionEvent{#GameMotionEvent}
动作事件

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| cancelled | boolean | 动作是否被中途打断 |
| tick | number | 事件发生时间 |
| target | [GameEntity](https://docs.dao3.fun/api/GameEntity/) | entity对象 |
| motionHandler | [GameMotionHandler](handler.md) | 本身的动作处理器 |

---
title: 商城与投喂
source: https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/shopping.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 商城与投喂
## 方法

#### <font id="API" />openMarketplace(<font id="Type">productIds:number[]</font>)<font id="Type">: void</font>{#openMarketplace}
打开游戏商店对话框，根据传入的“商品ID”显示相应的产品。

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| productIds | 是 | | number[] | 商品ID数组 |



**[details]**
```javascript
world.onPlayerJoin(({ entity }) => {
  // product ID1: 160000000000001  ID2: 160000000000002  
  entity.player.openMarketplace([160000000000001, 160000000000002])
});
```
---
---


#### <font id="API" />getMiaoShells()<font id="Type">: Promise‹number›</font>{#getMiaoShells}
获取此用户在当前地图下累计打赏的喵贝壳

**返回值**

| **类型** | **说明** |
| --- | --- |
| Promise‹number› | 异步返回当前玩家打赏的喵贝壳数量 |




**[details]**
```javascript
world.onPlayerJoin(async ({ entity }) => {
  // 获取用户在当前地图下累计打赏的喵贝壳
  const count = await entity.player.getMiaoShells()
  entity.player.directMessage(`我累计打赏的喵贝壳：${count}`)
})
```
---

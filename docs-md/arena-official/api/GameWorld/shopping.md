---
title: 小鱼干商城
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/shopping.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 小鱼干商城
**[warning]**
**💡值得注意的是：**

由于小鱼干商城功能涉及商业化，因此需要额外申请权限才可使用。

若你希望获得使用本API的权限，请前往QQ群：**478041977**，联系管理员：吉吉喵小助理，进行申请该权限。

---
### **方法**

#### <font id="API" /><font id="Event">事件</font>onPlayerPurchaseSuccess(<font id="Type">handler:(event:[GamePurchaseSuccessEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/shopping#GamePurchaseSuccessEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font> {#onPlayerPurchaseSuccess}
当玩家成功购买物品时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | _是_ | | function | 监听到玩家购买后的处理函数 |





**[details]**
```javascript
world.onPlayerPurchaseSuccess(({ userId, productId, orderId }) => {
  // 假如商城后台添加了此id的道具，功能为复活道具
  if (productId === 160000000000001) {
    // 由于可能存在多服的情况，每个服都会收到此购买成功的回调，因此需要判断当前服务器有此玩家
    const entity = world.querySelectorAll('player').filter(e => e.player.userId === userId)[0];
    if (entity) {
      entity.player.forceRespawn();
    }  
  }
});
```
---
## 接口

#### <font id="API" />GamePurchaseSuccessEvent{#GamePurchaseSuccessEvent}
**当玩家成功购买物品时触发的事件**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| tick | number | 购买成功事件发生的时间 |
| userId | string | 触发购买事件的玩家userId |
| productId | number | 购买商品的ID |
| orderId | number | 购买成功的订单号 |

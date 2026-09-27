---
title: 画面滤镜
source: https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/colorLUT.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 画面滤镜
## 属性

#### <font id="API" />colorLUT<font id="Type">: string </font>{#colorLUT}
> 默认值：''

用于渲染玩家所见游戏世界的色调



```javascript
world.onPlayerJoin(({ entity:{ player } }) => {
  // 玩家进入游戏的时候随机更改游戏世界的色调
  const luts = resources.ls('lut');
  const randLut = luts[(luts.length * Math.random()) | 0].path;
  player.directMessage('lut = ' + randLut)
  player.colorLUT = randLut;
});
```

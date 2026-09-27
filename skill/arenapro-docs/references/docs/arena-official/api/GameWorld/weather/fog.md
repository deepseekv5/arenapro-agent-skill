---
title: 天气-雾
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/fog.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 天气-雾

## 属性

#### <font id="API" />maxFog  <font id="Type">: number</font>{#maxFog}
> 默认值：1

最大雾量。



---


#### <font id="API" />fogColor <font id="Type">: [GameRGBColor](https://docs.dao3.fun/api/GameRGBColor/)</font> {#fogColor}
> 默认值：GameRGBColor(1, 1, 1)

雾的颜色。


---


#### <font id="API" />fogStartDistance  <font id="Type">: number</font>   {#fogStartDistance}
> 默认值：0

雾起始距离。



---


#### <font id="API" />fogHeightOffset  <font id="Type">: number</font>  {#fogHeightOffset}
> 默认值：0

雾高度。



---


#### <font id="API" />fogUniformDensity  <font id="Type">: number</font> {#fogUniformDensity}
> 默认值：0

均匀雾量，若值大于0，越难看到天空。



---


#### <font id="API" />fogHeightFalloff <font id="Type">: number </font>{#fogHeightFalloff}
> 默认值：0.8

高度衰减系数。数值在0-1之间。值越小，雾越浓。

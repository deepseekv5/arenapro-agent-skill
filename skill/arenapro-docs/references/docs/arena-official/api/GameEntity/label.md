---
title: 标识
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/label.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 标识
## 属性

#### <font id="API" />id<font id="Type">: string</font>{#id} 
> 默认值：无

已在编辑器中添加的实体名称




## 方法

#### <font id="API" />addTag(<font id="Type">tag:string</font>)<font id="Type">:  void</font>{#addTag} 
为实体添加一个新标签。

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| tag | 是 | | string | 要添加的标签名 |



---


#### <font id="API" />hasTag(<font id="Type">tag:string</font>)<font id="Type">: boolean</font>{#hasTag} 
判断实体是否带有某个标签。

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| tag | 是 | | string | 要检测的标签名 |

**返回值**

| **类型** | **说明** |
| --- | --- |
| boolean | 是否带有该实体标签 |



---


#### <font id="API" />removeTag(<font id="Type">tag:string</font>)<font id="Type">: void</font>{#removeTag} 
从实体移除标签。

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| tag | 是 | | string | 要移除的标签名 |



---


#### <font id="API" />tags()<font id="Type">: string[]</font>{#tags} 
获取编辑器中给实体添加的全部标签。

**返回值**

| **类型** | **说明** |
| --- | --- |
| string[] | 该实体的标签列表 |

---
title: 获取游戏资产树
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameAssetListEntry/ls.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 获取游戏资产树

## 方法

#### <font id="API" />ls(<font id="Type">path?:'snow' | 'mesh' |'picture' | 'audio' | 'lut'</font>)<font id="Type">: [GameAssetListEntry](https://github.com/box3lab/box3-product-document/blob/master/api/GameAssetListEntry/ls#GameAssetListEntry)[]</font>{#ls}
获取地图中的资产树

**输入参数**

| _**参数**_ | **_必填_** | **_默认值_** | **_类型_** | **_说明_** |
| --- | --- | --- | --- | --- |
| path |  | | 'snow' &#124; 'mesh' &#124; 'picture' &#124; 'audio' &#124; 'lut' | 文件夹名称，如果输入该值，会获取该文件夹下的全部文件。 |

**返回值**

| **类型** | **说明** |
| --- | --- |
| GameAssetListEntry[] | 资产列表，包含文件类型和路径 |



## 接口

#### <font id="API" />GameAssetListEntry{#GameAssetListEntry}
资产列表

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| path | string  | 资产的完全限定路径，按目录拆分 |
| type | [GameAssetType](https://github.com/box3lab/box3-product-document/blob/master/api/GameAssetListEntry/ls#GameAssetType)  | 资产类型 |




## 枚举

#### <font id="API" />GameAssetType{#GameAssetType}
资产类型

| **属性** | **说明** |
| --- |  --- |
| VOXEL_MESH  | 模型  |
| DIRECTORY  | 文件夹  |
| COLOR_LUT  |  颜色滤镜 |
| JS_SCRIPT  | 脚本  |
| IMAGE  |  图片 |
| PARTICLE_TEXTURE  | 雪花纹理  |
| SOUND  | 音频  |
| PICTURE   |  图片 |

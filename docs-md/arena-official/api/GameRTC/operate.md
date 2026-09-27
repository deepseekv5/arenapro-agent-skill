---
title: 操作
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameRTC/operate.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 操作

## 方法
#### <font id="API" />getMicrophonePermission(<font id="Type">entity:[GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer)</font>)<font id="Type">: Promise‹boolean›</font>{#getMicrophonePermission}
向该通道申请获取一个玩家的录音权限

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| entity | 是 |  | string | 玩家对象 |


**返回值**

| **类型** | **说明** |
| --- | --- |
| Promise‹boolean› | 异步返回是否成功获取到录音权限 |



---
#### <font id="API" />add(<font id="Type">entity:[GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer)</font>)<font id="Type">: Promise‹void›</font>{#add}
向该通道加入一个玩家

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| entity | 是 |  | string | 玩家对象 |




---
#### <font id="API" />remove(<font id="Type">entity:[GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer)</font>)<font id="Type">: Promise‹void›</font>{#remove}
向该通道删除一个玩家

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| entity | 是 |  | string | 玩家对象 |




---
#### <font id="API" />unpublish(<font id="Type">entity:[GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer)</font>)<font id="Type">: Promise‹void›</font>{#unpublish}
向该通道一个玩家关闭麦克风

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| entity | 是 |  | string | 玩家对象 |




---
#### <font id="API" />publishMicrophone(<font id="Type">entity:[GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer)</font>)<font id="Type">: Promise‹void›</font>{#publishMicrophone}
向该通道一个玩家开启麦克风

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| entity | 是 |  | string | 玩家对象 |




---
#### <font id="API" />getPlayers()<font id="Type">: Promise‹[GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer)[]›</font>{#getPlayers}
获取该通道目前所有的玩家

**返回值**

| **类型** | **说明** |
| --- | --- |
| Promise‹GamePlayerEntity[]› | 异步返回玩家对象列表 |




---
#### <font id="API" />destroy()<font id="Type">: Promise‹void›</font>{#destroy}
删除该通道



---
#### <font id="API" />getVolume(<font id="Type">entity:[GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer)</font>)<font id="Type">: Promise‹number›</font>{#getVolume}
获取该通道一个玩家音量

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| entity | 是 |  | string | 玩家对象 |

**返回值**

| **类型** | **说明** |
| --- | --- |
| Promise‹number› | 异步返回音量大小 |



---
#### <font id="API" />setVolume(<font id="Type">entity:[GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer),volume:number</font>)<font id="Type">: Promise‹void›</font>{#setVolume}
向该通道设置一个玩家音量

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| entity | 是 |  | string | 玩家对象 |
| volume | 是 |  | number | 音量大小 |

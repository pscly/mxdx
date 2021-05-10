# 实训1

## 要求

1. 输出所有图书的信息:包括每本书的编号、书名、单价、库存
2. 顾客购买书:根据提示输入图书编号来购买书,并根据提示输入购买书的的数量
3. 购买完毕后输出顾客的订单信息:包括订单号、订单明细、订单总额

## 类设计

![](md-images/2021-05-10-10-55-52.png)

## 问题

1. 数据库那边，我保存数据库的时候我会直接把原来的数据库删除了，免得更新出问题(主要是懒得写，麻烦)
   1. 当然，这就导致了一个问题，每次数据库更新都要带着原来的数据，因为是直接覆盖
   2. 当然有其他解决方法，先保存一次读取的，然后判断，分割
   3. **创个新表，下次读取新表**
      1. 运行多少次就创建多个表

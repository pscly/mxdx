# coding: utf-8
# 持久化
# 数据保存到哪

from conn_mongo import MyMongo1

def to_mongo(data, table):
    '''
    data: data应该是[字典] 
    table: 是表名(例如book,)
    '''
    mongo1 = MyMongo1(table)
    mongo1.save([data])

print('')
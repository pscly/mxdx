# coding: utf-8
# 持久化
# 数据保存到哪

from conn_mongo import MyMongo1

def drop_mongo(table=None, mongo1=None):
    '''
    要么是表名，要么是对象,至少放一个, mongo1优先度更高

    table: 表名
    mongo1: mongo数据库对象
    '''
    if not mongo1:  # 如果没有传mongo对象进来
        mongo1 = MyMongo1(table)
    mongo1.drop_datas()

def to_mongo(data, table):
    '''
    data: data应该是 列表套字典, 如果不是列表，就会自动套上[]
    table: 是表名(例如book,)
    '''
    mongo1 = MyMongo1(table)

    # 先删除一下原本的数据
    # drop_mongo(table=table) # 使用表名
    drop_mongo(mongo1=mongo1) # 使用mongo对象

    if isinstance(data, list):
        mongo1.save(data)
    else:
        mongo1.save([data])

print('')

def load_mongo(table, tj={}):
    '''
    table: 表名
    tj: 查询条件
    return: [{},{}]
    '''
    mongo1 = MyMongo1(table)

    return mongo1.find(tj)

if __name__ == '__main__':
    # to_mongo([{'_id': '1', 'name': 'pscly', 'price': 310}, {'_id': '2', 'name': 'lsy', 'price': 31.01}], 'test1')
    x1 = load_mongo('test1')
    print(x1)

# coding: utf-8
# 持久化
# 数据保存到哪

from conn_mongo import MyMongo1


def to_mongo(data, table):
    '''
    data: data应该是 列表套字典, 如果不是列表，就会自动套上[]
    table: 是表名(例如book,)
    '''
    mongo1 = MyMongo1(table)

    if isinstance(data, list):
        mongo1.save(data)
    else:
        mongo1.save([data])

    import time
    print('快删除了')
    time.sleep(10)
    mongo1.drop_datas()
    print('删除成功了')

print('')

def load_mongo(table, tj={}):
    '''
    table: 表名
    tj: 查询条件
    return: [{},{}]
    '''
    mongo1 = MyMongo1(table)
    mongo1.find(tj)

if __name__ == '__main__':
    to_mongo([{'_id': '1', 'name': 'pscly', 'price': 30}, {'_id': '2', 'name': 'lsy', 'price': 21.01}], 'test1')

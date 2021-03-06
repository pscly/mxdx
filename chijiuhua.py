# coding: utf-8
# 持久化
# 数据保存到哪

from conn_mongo import MyMongo1
import os
import json

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

def load_mongo(table, tj={}):
    '''
    table: 表名
    tj: 查询条件
    return: [{},{}]
    '''
    mongo1 = MyMongo1(table)

    return mongo1.find(tj)

def to_json(data, table):
    '''
    保存到json文件
    data: 要保存的数据，格式:[{}]
    table: 文件名(数据的类名), 应该是字符串
    '''
    with open(f'./data/{table}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def load_json(table, tj={}):
    '''
    从json文件中读取数据
    table: 要读取的表名, 应该是字符串
    tj: 读取的条件
    '''
    if not os.path.isfile(f'./data/{table}.json'):
        print('数据文件不存在')
        
        if not os.path.isdir('./data'):
            os.makedirs('data')

        with open(f'./data/{table}.json', 'w', encoding='utf-8') as f:
            json.dump('', f)
        print('已经为你初始化了数据文件')
        raise Exception('\n'+'*'*60+'\n'+table+'数据不存在, 已经自动创建，但是需要手动重启程序')

    with open(f'./data/{table}.json', 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    # # to_mongo([{'_id': '1', 'name': 'pscly', 'price': 310}, {'_id': '2', 'name': 'lsy', 'price': 31.01}], 'test1')
    # x1 = load_mongo('test1')
    # print(x1)
    # to_json([{'_id': '1', 'name': 'pscly', 'price': 310}, {'_id': '2', 'name': 'lsy', 'price': 31.01}], 'xx1')
    
    x1 = load_json('xx21')
    print(x1)


from pymongo import MongoClient


class MyMongo1():

    def __init__(self, table):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['mxdx1']
        self.table_user = self.db[table]

    def drop_datas(self):
        self.table_user.drop()

    def save(self, data):
        '''
        data: data应该是[字典] 
        '''
        self.table_user.insert_many(data)
        # print(table_user.count())

    def update(self, tiaojian, data):
        '''
        更新数据
        tiaojian: 更新条件
        data: 更新数据的数据
        '''
        self.table_user.update(data)

    
    def find(self, tj):
        '''
        查找书籍
        tj: 查找书籍的条件
        return 返回的东西需要for循环才能查询
        '''

        # print(table_user.find_one({}))
        l1 = []
        x = self.table_user.find(tj)  # 这个又是相当于是普通的find，返回对象，需要for
        for i in x:
            l1.append(i)
        return l1

# coding: utf-8
# 这里存放我的class

from chijiuhua import load_json, to_json, to_mongo, load_mongo

class Book():
    books = []  # 书的对象s
    books_id = []
    books_del_id = []


    def __init__(self, name, price, shuliang, is_del=0, **kwargs):
        self._id = len(self.books)+1   # 书籍的id是当前书籍的+1
        self.name = name
        self.price = price
        self.shuliang = shuliang
        self.is_del = is_del    # 书籍是否是删除
        self.add_s(self)

    @classmethod
    def add_s(cls, self):
        '''
        
        cls: 是类(这玩意会自动传进来)
        self: 是类实例化的当前对象
        将书籍s保存到Book,books，方便后面读取
        '''
        cls.books.append(self)
        if self.is_del:
            cls.books_del_id.append(self._id)
        else:
            cls.books_id.append(str(self._id))
        # 在添加书籍的时候就把数据保存到数据库
        # TODO读取就保存数据库
        # cls.save_book()
        
    @classmethod
    def new1(cls):
        '''创建书'''
        print('书籍的id，将会自动生成')
        name = input('请输入书籍的名字:').strip()
        
        price = input('请输入书籍的价格:').strip()
        if not price.isdigit():
            print('价格输入有误')
        if int(price) < 0:
            print('价格不能低于0')
            
        shuliang = input('请输入书籍的数量:').strip()
        if not shuliang.isdecimal():
            print('数量输入有误')
        if int(shuliang) < 0:
            price('数量不能低于0')

        return cls(name, int(price), int(shuliang))

    @classmethod
    def del1(cls):
        '''删除书的方法'''
        while 1:
            cls.looks()

            in_book = input('请输入你要删除的书籍的id(输入q退出):').strip()

            if in_book.lower() == 'q':
                return

            if not in_book.isdigit():
                print('输入有误')
                continue
            in_book = int(in_book)

            for i in cls.books:
                if in_book == i._id:
                    i.is_del = 1
                    print('删除成功')
                    cls.del_s(in_book)
                    return
            print('没有找到这个书籍')

    @classmethod
    def find(cls, _id):
        '''
        查看指定书籍是否存在
        _id: 指定书籍的id(编号)，可以是列表
        return: 如果书存在就返回那本书的对象，不存在就会返回None或者空列表
        '''
        if isinstance(_id, list):
            book_l1 = []
            for book_id in _id:
                for book in cls.books:
                    if book._id == book_id:
                        book_l1.append(book)
                        break
            return book_l1
        

        for book in cls.books:
            if book._id == _id:
                return book

    @classmethod
    def del_s(cls, _id):
        '''
        去删除当前的书籍列表
        _id: 要删除的那个书籍的id
        '''
        # cls.books.pop(_id-1)  # !如果这个也删除了，数据库中就也会删除这本书
        cls.books_id.pop(_id-1)

    @classmethod
    def load(cls):
        '''
        从数据库读取书籍，这个东西应该是程序运行开始的时候运行
        '''
        # books = load_mongo(cls.__name__)
        books = load_json(cls.__name__)

        for book in books:
            # if book.get('is_del'):
            #     continue
            b1 = cls(**book)
        return 

    @classmethod
    def save(cls):
        '''
        这玩意会把类里面的所有书籍保存到数据库
        '''
        l1 = []
        for book in cls.books:
            # print(book)
            l1.append(book.get_data())
        # to_mongo(l1, cls.__name__)
        to_json(l1, cls.__name__)
        print(cls.__name__, '保存成功')

    def get_data(self):
        return {
            '_id':self._id,
            'name':self.name,
            'price':self.price,
            'shuliang':self.shuliang,
            'is_del':self.is_del
        }

    @classmethod
    def looks(cls, is_del=0):
        '''
        查看当前所有书籍，并且打印出来
        '''
        print('-'*90)
        print('书籍id\t书籍名称\t书籍单价\t书籍数量\t'.expandtabs(21))
        for book in Book.books:
            if is_del == book.is_del:
                print(f'{book._id}\t{book.name}\t{book.price}\t{book.shuliang}\t'.expandtabs(24))
        print('-'*90)

class Dingdan():
    dingdans = []  # 书的对象s
    dingdans_id = []

    def __init__(self, book_name, book_shuliang, zongjia, **kwargs) -> None:
        self._id = len(Dingdan.dingdans) + 1
        self.book_name = book_name
        self.book_shuliang = book_shuliang
        self.zongjia = zongjia
        self.add_s(self)

    @classmethod
    def add_s(cls, self):
        '''将订单放到列表中'''
        cls.dingdans.append(self)
        cls.dingdans_id.append(self._id)
        
    @classmethod
    def new1(cls):
        '''创建订单'''
        print('订单的id，将会自动生成')
        Book.looks()
        while 1:
            # 此循环是为了找到书
            while 1:
                # 此循环是为了正确的输入
                book_id = input('请输入书籍的编号(输入q退出):')
                if book_id.lower() == 'q': 
                    return
                if book_id.isdecimal():
                    book_id = int(book_id)
                    if book_id < 0:
                        print('数量不能小于0')
                        continue
                    break
                print('输入有误')
            book = Book.find(book_id)
            if not book:
                print('书籍不存在')
                continue
            print(f'书籍: {book.name}')
            break

        # TODO 查找书籍
        while 1:
            # 为了正确的输入
            count = input(f'请输入书籍的数量(当前数量({book.shuliang})):')
            if count.isdigit():
                count = int(count)
                if count <= book.shuliang:
                    book.shuliang -= count
                    break
                print('我这边没有那么多书啊……')
            print('没有那么多书')
        
        jiaqian = book.price * count
        print(f'总价是{jiaqian}')
        return cls(book.name, count, jiaqian)

    
    @classmethod
    def load(cls):
        '''
        从数据库读取订单，这个东西应该是程序运行开始的时候运行
        '''
        dingdans = load_json(cls.__name__)

        for dingdan in dingdans:
            # if book.get('is_del'):
            #     continue
            b1 = cls(**dingdan)
        return 

    
    @classmethod
    def looks(cls):
        '''
        查看当前所有订单，并且打印出来
        '''
        print('-'*90)
        print('订单号\t书籍名称\t书籍数量\t总价\t'.expandtabs(21))
        for dingdan in Dingdan.dingdans:
            print(f'{dingdan._id}\t{dingdan.book_name}\t{dingdan.book_shuliang}\t{dingdan.zongjia}\t'.expandtabs(24))
        
        print('-'*90)

    def get_data(self):
        return {
            '_id': self._id,
            'book_name': self.book_name,
            'book_shuliang': self.book_shuliang,
            'zongjia': self.zongjia,
        }

    @classmethod
    def save(cls):
        '''保存订单'''
        l1 = []
        for dingdan in cls.dingdans:
            l1.append(dingdan.get_data())
        
        # to_mongo(l1, cls.__name__)
        to_json(l1, cls.__name__)
        print(cls.__name__, '保存成功')
        


def select_func():
    l1 = []
    for count,func in Book.book_funcs:
        l1.append([str(count), func])
    
def save_all(*args):
    '''
    *args: 这个东西是吧指定的类传入，然后保存类下的所有东西
    '''
    if not args:
        args = [Book, Dingdan]
    for cls in args:
        cls.save()

def load_all(*args):
    '''
    *args: 这个东西是吧指定的类传入，然后读取类下的所有东西
    '''
    if not args:
        args = [Book, Dingdan]
    for cls in args:
        cls.load()


funcs = [
    [Book.looks, ['查看所有书籍']],
    [Book.new1, ['新建书籍']],
    [Book.del1, ['删除书籍']],
    [Dingdan.looks, ['查看所有的订单']],
    [Dingdan.new1, ['新建订单(买书)']],
    [save_all, ['保存']],
]

if __name__ == '__main__':
    # Book.load()
    # load_all(Book)
    load_all(Book, Dingdan)
    # x = Book.find_book([1,2121])
    # if not x: print('空')
    # print(x)
    # a1 = Book('python入门', 10.99, 300)
    # a2 = Book('python高级', 20.00, 30)
    # a3 = Book('java入门', 30.00, 90)
    # # Book.look_books()
    # Book.new_book()
    # Book.look_books(1)
    # Book.del_book()
    # lfr
    # Dingdan.new1()
    # Dingdan.
    Book.looks()
    Dingdan.looks()
    # Dingdan.new1()
    # Dingdan.looks()
    # print()
    # test_gitee
    # Book.save()
    save_all(Book, Dingdan)
    # Book.look_books()
    # Book.del_books()


# coding: utf-8
# 这里存放我的class

from chijiuhua import to_mongo, load_mongo

class Book():
    books = []  # 书的对象s
    books_id = []


    def __init__(self, name, price, shuliang, **kwargs):
        self._id = len(self.books_id)+1   # 书籍的id是当前书籍的+1
        self.name = name
        self.price = price
        self.shuliang = shuliang
        self.is_del = 0    # 书籍是否是删除
        self.add_Book_books(self)

    @classmethod
    def add_Book_books(cls, self):
        # 将书籍s保存到Book,books，方便后面读取
        cls.books.append(self)
        cls.books_id.append(str(self._id))
        # print(cls.books)
        # 在添加书籍的时候就把数据保存到数据库
        cls.save_book()
        
    @classmethod
    def new_book(cls):
        # 创建书
        print('书籍的id，将会自动生成')
        name = input('请输入书籍的名字:')
        price = input('请输入书籍的价格:')
        shuliang = input('请输入书籍的数量:')
        return cls(name, price, shuliang)

    @classmethod
    def del_book(cls):
        while 1:
            cls.look_books()

            in_book = input('请输入你要删除的书籍的id(输入q退出):').strip()

            if in_book.lower() == 'q':
                return

            if not in_book.isdigit():
                print('输入有误')
                continue
            in_book = int(in_book)
            
            # print(cls.books_id)

            # if in_book in cls.books_id:
            #     print('书籍不存在')
            #     continue

            # TODO 删除书籍
            for i in cls.books:
                print(i._id)
                print(type(i._id))
                if in_book == i._id:
                    i.is_del = 1
                    print('删除成功')
                    cls.def_now_book(in_book)
                    return
            print('没有找到这个书籍')

    @classmethod
    def def_now_book(cls, _id):
        '''
        去删除当前的书籍列表
        _id: 要删除的那个书籍的id
        '''
        cls.books.pop(_id-1)
        cls.books_id.pop(_id-1)

    @classmethod
    def load_book(cls):
        '''
        从数据库读取书籍，这个东西应该是程序运行开始的时候运行
        '''
        # 读取书
        # def load_book(self, id, name, price, shuliang):
        books = load_mongo(cls.__name__)

        for book in books:
            if book.get('is_del'):
                continue
            b1 = cls(**book)
        return 

    @classmethod
    def save_book(cls):
        '''
        这玩意会把类里面的所有书籍保存到数据库
        '''
        # 持久化2
        l1 = []
        for book in cls.books:
            # print(book)
            l1.append(book.get_data())
        to_mongo(l1, cls.__name__)

    def get_data(self):
        return {
            '_id':self._id,
            'name':self.name,
            'price':self.price,
            'shuliang':self.shuliang
        }

    @classmethod
    def look_books(cls):
        '''
        查看当前所有书籍，并且打印出来
        '''
        print('-'*72)
        print('书籍id\t书籍名称\t书籍单价\t书籍数量\t'.expandtabs(21))
        for book in Book.books:
            print(f'{book._id}\t{book.name}\t{book.price}\t{book.shuliang}\t'.expandtabs(24))


    # Book的方法
    book_funcs = [
        [look_books, ['查看当前所有书籍']],
        [new_book, ['新建书籍']],
        [del_book, ['删除书籍']],
        # save_book, ['把当前数据保存到数据库'],   
    ]

def select_func():
    l1 = []
    for count,func in Book.book_funcs:
        l1.append([str(count), func])

if __name__ == '__main__':
    Book.load_book()
    # a1 = Book('01', 'python入门', 10.99, 300)
    # a2 = Book('02', 'python高级', 20.00, 30)
    # a3 = Book('03', 'java入门', 30.00, 90)
    # Book.look_books()
    # Book.new_book()
    # Book.look_books()
    Book.del_book()

    Book.save_book()
    Book.look_books()
    # Book.del_books()


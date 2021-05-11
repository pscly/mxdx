# coding: utf-8
# 这里存放我的class

from chijiuhua import to_mongo
from chijiuhua import load_mongo

class Book():
    books = []  # 书的对象s
    books_id = []

    def __init__(self, _id, name, price, shuliang):
        if _id in Book.books_id:
            raise Exception('书籍编号已经有了')
        self._id = _id
        self.name = name
        self.price = price
        self.shuliang = shuliang
        self.add_Book_books(self)

    @classmethod
    def add_Book_books(cls, self):
        cls.books.append(self)
        cls.books_id.append(self._id)
        print(cls.books)
        
    @classmethod
    def new_book(cls):
        # TODO
        # 创建书
        _id = input('请输入书籍的id:')
        name = input('请输入书籍的名字:')
        price = input('请输入书籍的价格:')
        shuliang = input('请输入书籍的数量:')
        return cls( _id, name, price, shuliang)

    @classmethod
    def load_book(cls):
        # def load_book(self, id, name, price, shuliang):
        books = load_mongo(cls.__name__)

        for book in books:
            b1 = cls(**book)
        return 
        # TODO
        # 读取书
        pass

    @classmethod
    def save_book(cls):
        '''
        这玩意会把类里面的所有东西都会保存
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


if __name__ == '__main__':
    # a1 = Book('01', 'python入门', 10.99, 300)
    # a2 = Book('02', 'python高级', 20.00, 30)
    # a3 = Book('03', 'java入门', 30.00, 90)
    Book.load_book()
    # print(Book.books)

    a4 = Book('05', 'c++真不错,', 19.99, 20)
    if not a4:
        print('输入有误， 书籍有误')
    Book.save_book()

    # print(Book.books)
    print('书籍id\t|书籍名称\t书籍单价\t书籍数量\t'.expandtabs(18))
    for book in Book.books:
        print(f'{book._id}\t|{book.name}\t{book.price}\t{book.shuliang}\t'.expandtabs(20))
        # print(book._id, book.name,book.price, book.price)
    # print(a4.save_book())


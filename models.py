# coding: utf-8
# 这里存放我的class

from chijiuhua import to_mongo

class Book():
    books = []  # 书的对象s 

    def __init__(self, id, name, price, shuliang):
        self.id = id
        self.name = name
        self.price = price
        self.shuliang = shuliang
        self.add_Book_books(self)
        
    def __init__(self):
        self.add_Book_books(self)
    

    @classmethod
    def add_Book_books(cls, self):
        cls.books.append(self)
        print(cls.books)
        
    def new_book(self, id, name, price, shuliang):
        # TODO
        # 创建书
        pass

    def load_book(self, id, name, price, shuliang):
        # TODO
        # 读取书
        pass

    @classmethod
    def save_book(cls):
        # TODO 
        # 持久化2
        l1 = []
        for book in cls.books:
            # print(book)
            l1.append(book.get_data())
        to_mongo(l1, cls.__name__)

    def get_data(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'storage':self.storage,
        }


if __name__ == '__main__':
    

    a1 = Book()
    a2 = Book()
    a4 = Book()
    a4 = Book()
    a4 = Book()

    print(Book.books)
    print(a4.save_book())


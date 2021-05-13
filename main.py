from models import Book, Dingdan, save_all,load_all, funcs

def look_funcs(funcs):
    ''' 
    查看所有的方法，然后自动编号然后放到字典中返回
    return: {编号, [函数地址, 函数注释]}
    '''
    d1 = {}
    for i, func in enumerate(funcs, 1):
        print(i, func[1][0])
        d1[str(i)] = [func[0], func[1]]
    return d1

def choose_func(funcs):
    while 1:
        d1 = look_funcs(funcs)
        in1 = input('请输入你要选择的功能(q退出):').strip()
        if in1.lower() == 'q':
            exit('退出')
        if in1 in d1:
            d1[in1][0]()

if __name__ == '__main__':  
    choose_func(funcs)

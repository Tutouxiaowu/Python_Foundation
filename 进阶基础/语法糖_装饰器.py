def func_1(func):
    print('这里是fun_1方法')
    return func() # 返回的是方法

def say():
    print('fxxckpython')

func_1(say) # 这里不能写say() 因为这样写的话，返回的是none 即func_1(none)
# print(func_1(say)) # 结构为 fxxckpython 和 none


# 错误 say没有返回值得到是none
# s =  say()

# 想要解决这样的尴尬，我们可以定义一个内部方法，然后返回这个引用，像这样：
def func_2(func):
    def inner_func():
        print(f'{func}执行前操作')
        func()
        print(f"{func}执行后操作")
    return inner_func # 内部返回这个引用

my_func = func_2(say)
my_func()

def login_user(username,passwd):
    print("login success")
    # 其实这里也可以设置一个返回值
def user_check(func):
   def wrapper(username,passwd):
       if(username != 'root'):
           # 自定义异常 raise
           raise  Exception('permission denied')
       elif(passwd != 'admin'):
           raise Exception('passwd incorrect')
       else:
           return func(username,passwd) #
       #分支 if elif else -->其中elif 相当于else if
   return wrapper # 函数返回的wrapper

login = user_check(login_user) # login 得到的是 wrapper方法
login('root','admin') # 传入参数 给wrapper


# 但是这样麻烦的
# 可以直接这样使用，在 @ 后面添加一个你要进行额外操作的方法名称。
@user_check # 装饰器：接收另一个函数，然后扩展这个函数的行为而不是显示的直接修改它。
def login_new_user(username,password):
    print('ojbk')
login_new_user('root','admin')
# 即这个函数（或者说方法）被装饰器 user_check 接收 相当于 user_check(login_user)


# 再往下拓展
# 装饰器再定义的同时 还可以给它传参数


def check(length):  #这样一个修饰器
    def user_check(func):
       def wrapper(username,passwd):
           if(username != 'root'):
               # 自定义异常 raise
               raise  Exception('permission denied')
           elif(passwd != 'admin6'):
               raise Exception('passwd incorrect')
           elif(len(passwd)<length):
               raise Exception(f'passwd must be at least {length} c')
           else:
               return func(username,passwd) #
           #分支 if elif else -->其中elif 相当于else if
       return wrapper # 函数返回的wrapper
    return user_check

@check(6)
def new_login(username,passwd):
    print('这次终于对了')
new_login('root','admin6')

'''
话说回来，decorator（装饰器）是一种特殊的函数，它的目的在于修改或加强其他函数
的功能它可以在 不修改原来的代码的基础上，进行@语法糖修饰。
简单的来说，就是，@接收一个函数，再对它进行更改

'''




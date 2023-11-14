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


# 但是这样麻烦的
# 可以直接这样使用，在 @ 后面添加一个你要进行额外操作的方法名称。
@user_check # 装饰器：接收另一个函数，然后扩展这个函数的行为而不是显示的直接修改它。
def login_new_user(username,password):
    print('ojbk')
login_new_user('root','admin')
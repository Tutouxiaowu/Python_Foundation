# 虽然是基础但是在课堂上，老师对于，with的用法也只是寥寥草草的几个 with open.下面是对with比较全面的解释
#with : 一般来说，想要被with调用需要 __enter__()与 __exit__()
#举个栗子@。@
#创建对象
class duixiang:
    def __enter__(self):
        print('进入enter方法')
        return 6666
    def __exit__(self, exc_type, exc_val, exc_tb):#注意到这几个参数exc_.异常0.o有没有像谐音
        print('进入exit方法')
    def __zhix__(self):
        print("执行中")
        return 8888
#利用方法进行调用
def function():
    return duixiang()
with function():
    print(function().__zhix__())
#with as f  f得到什么呢？
print()
print()
with function() as f:
    print(f)
#如程序结果，得到的是，enter的返回值
#ok 说回exit中几个特殊的返回值
class duixiang:
    def __enter__(self):
        print('进入enter方法')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):#注意到这几个参数exc_.异常0.o有没有像谐音
        print('进入exit方法')
        print('type',exc_type)
        print('value',exc_val)
        print('traceback',exc_tb)
    def __zhix__(self):
        print("执行中")
        return 100/0
def function():
    return duixiang()
with function() as f:
    f.__zhix__()
#是的得到异常
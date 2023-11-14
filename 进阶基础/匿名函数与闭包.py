## 匿名函数 lambda
def add_self(x):
    return x+1
(lambda x:x+1)(5)# 参数的传递
# 像这种都是用一次就丢弃了，写法更加简洁高效
# 所以平常都是结合map filter函数使用
list1 = [1,2,3,4,5,6,7,8]
print(list(map(add_self,list1)))# 将list1 映射（map）到add_self方法中
print(list(map(lambda x:x+1,list1)))# 更加简洁
# filter 也一样
print(list(map(lambda x:x%2==0,list1)))
def add_self1(x):
    return x+1
def add_self2(x):
    print(x+1)

print(add_self1(5)) # 这相当于将 执行方法后返回的对象 放入print方法执行
print(add_self2(5)) # 这里因为没有返回值，所以为空，才会print none值
# 如果返回值 为函数本身呢?
def add_self3(x):
    if x == 100:
        return x
    x = x+1
    print(x)
    return add_self3(x)
print(add_self3(1)) # 是否变成了递归了呢
# 如果是再嵌套函数里面继续返回函数本身呢
def out_fun(x):
    def in_fun():
        # x =  x +1 不行，因为不能用外部变量 此时应该加上nonlocal
        nonlocal x
        x = x + 1
        print(x)
    in_fun()
out_fun(6)


def outer_fun(x):
    def inner_fun():
        print(x+1)
    return inner_fun # 返回函数方法
outer =  outer_fun(5) # 此时outer得到的是一个函数方法
outer() # 执行

def outer_fun2(x):
    def inner_fun(y):
        print(x+y)
    return inner_fun # 返回函数方法
outer =  outer_fun2(5) # 此时outer得到的是一个函数方法def inner_fun(y)
outer(7) # 传入参数y 执行
# 以上操作即是 闭包



######
# 注意上述这段代码：print(list(map(lambda x:x%2==0,list1)))
my_list1 = list(filter(lambda x:x%2==0,list1))
# 其实我也可以直接用类似简短的代码生成
my_list2 = [i for i in range(1,15)if i%2==0] # 即表达式
# [表达式 循环语句 条件]
my_list3 = ['what','is','the','fuckpython','nice']
new_list = [str.upper() for str in my_list3]
print(new_list)
age = 18
def my_func():
   name = "wc"
   # age = age + 1 函数内不可以直接用外部的全局变量
   # 可以这个样子
   global age # 指的就是全局变量的age
   print(age+1)
   print(name)
my_func()
# 另外nonlocal可以在被窃入的函数中使用
def change_list(list):
    list = [1,'fxxk',3,4]
my_list = [1,2,3,4]
change_list(my_list)
print(my_list)
def print_some(length,*factor):# 但我们不知道后面将要设置多少个参数时，可以加* 表示可变参数
    print(f"factor:{factor}")
    print(f"length:{length}")
print_some(18,'唱','跳','rap','篮球')
import os
import sys
# 请在此输入您的代码
# n=input()
# a=list(map(int,input().split()))
# print(*sorted(a))
# print(*sorted(a,reverse=True))
#### 参数解包
def add(a,b):
  print(a+b)
l = [1,2]
add(*l) # 参数解包 将1,2 放入add方法中 如果是字典则用**
# 如上 print(*sorted(a))
# 将排列后的sort解包至 print方法中
# 转义字符 \n \t \r
###### 字符串的格式化
# 两种
print('大家好，我叫{},我今年{}岁！'.format('xiaoshuaibi','18'))
name = 'daxiaobi'
age = '18'
print(f'大家好，我叫{name},今年{age}')
##### String 的替换
str1  = "OK,让我们学习有关字符串的知识，虽然我很不想学"
print(str1)
str2 = str1.replace('不想学','想学')
print(str1)
print(str2)
# 由上，不知道你有没有发现，string类型是不可变的，即使使用了replace
## 字符串的分割 split
print(str2.split(','))# 得到的是，以逗号分隔开的，列表
####string的空格 
str3 = '''
   曹小华
'''
print(str3)
print(str3.strip())
##### 字符串的大小写转换，可以用lower和upper来转换
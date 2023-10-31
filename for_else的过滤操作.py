#for_else 没学过吧，我也没学过  =。=
#上代码：
def fun1():
   for i in range(1,5):
      print(i)
   else:
      print('执行完毕')
# fun1()
#结合contine和break呢
#判断你输入的数，是否有目标值
def input_list_int(list_str):#方法1
  list_int = list_str.split(",")
  for el in range(len(list_int)):
      list_int[el] = int(list_int[el])#这一操作其实可以：list_int = [int(x) for x in list_str]
  return list_int
x = 10
list_str = input("请输入整数数组，以,间隔:")
list = input_list_int(list_str)
for el in list:
    if el == x :
        print(f"哦豁，找到了目标值{el}了")
        break
else :
    print("达咩，没有找到目标值哦")
#类似的也有判断奇数偶数，质数
for i in range(2,10):
    for x in range(2,i):
        if i % x  == 0:
            print(i,"不是质数哦，因为它被本身整除外，还能被这样：",x,'*',int(i/x))
            break
        else:
            print(i,'我靠，不管，这tm就是质数')

##突然想起如何输入一个整数列表
def map_list_int(list_str):#方法2
    list_str1 = list_str.split(",")
    list_int = list(map(int,list_str1))#map地图嘛，可以理解为映射，将list_str1中的元素映射到“方法”int中。
    return list_int
# print(input_list_int(list_str))
# str = input("请输入一个包含若干整数的列表，各整数之间用,分隔：")
# int_list = eval("[" + str + "]")
# print(int_list)
#说到eval():1.将字符串当成有效的表达式来求值，并返回计算结果2.将字符串转换为字典或者列表
#就像下面一样：print(eval("1+1"))#2
# print(eval("'@'*5"))#@@@@@



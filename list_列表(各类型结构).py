# list_列表
# 初始化
list1 = []
list2 = [1,2,3,5,8,7,89]
# 基本操作
# 查
list2[2]
# 改
list2[2] = 4 #1,2,4
# 删
del list2[2]#删除下标为2的元素
list2.remove(1)#删除1这个元素 此时仅仅剩下一个元素咯[2]
list2.pop(0) # 删除仅剩的一个元素 pop（index）
# 增
list2.append(7)# 在后面扩充append 2
list2.insert(2,1)# 在下标为2的位置 插入1
#当然也可以采用列表相加
list2 = list2 +[2]
##list常用操作
# enumerate 获取坐标和相关的值
for i,v in enumerate(list2):
    print(f"{i}:{v}")
#追加单一数据append  扩展(多个)数据extend
#删除全部数据 list.clear()
#获取数据在列表中出现的次数：list.count(2)
#排序sort key reverse
#正序
list2.sort(reverse=False)
print(list2)
#逆序
list2.sort(reverse=True)
print(list2)
#逆序或者是list.reverse()
#s=key
# 你可以根据你的需求排序，比如按长度排序，那么可以先定一个方法：
# def length(item):
#     return len(item)
# 接着把函数作为参数传入 sort 中的 key 中：
# list2.sort(key=length)
# 当然也可以使用匿名函数
# list2.sort(key=lambda item : len(item))#字符串数组
# 复制
list3 = list2.copy()
#########
#元组操作和列表类似的，但是元组不可更改
#首先元组和列表都可以村组不同类型的数值
my_tuple = (1,0.2,'pikanoeat','p')
my_list = [1,0.2,'pikanoeat','p']
#首先看看其内存
print(my_tuple.__sizeof__())
print(my_list.__sizeof__())
# 这是因为列表需要更多的空间来 维持更改，而元组不需要（当数据固定时应更多的使用元组）
# 其间更改也很简单
my_list1 = list(my_tuple)
my_tuple1 = tuple(my_list)
#######
#字典
#如你所见以下为字典： key:value ->这里的key不可变，value可变
dict = {'name':'piaknoeat','age':18}
# 查
dict['name']# 通过key值来查找
print(list(dict))# 获得key值列表
# 改 ：已知仅有vale可改
dict['name'] = 'wc'
# 删 1.del dict['name'] 2.clear 3.del dict
# 增 指定
dict['high'] = 180
## 那么字典和元组，列表如何转换呢
list = dict.keys()
tuple = dict.items()
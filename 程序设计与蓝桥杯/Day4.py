'''
生物竞赛（B）选拔化学和数学总分最高的同学，信息学竞赛（I）选拔物理和数学总分最高的同学，党史竞赛（H）选拔政治和历史总分最高的同学，
现在给出N名同学的各科成绩，请编写程序帮忙选出适合参加相应竞赛的同学。
输入说明：
第一行包括一个整数N和一个字符C，N表示参与选拔的同学人数，C表示选择的竞赛类型。
输出说明：
适合指定竞赛类型的学生学号。如果有多个符合条件的学生，按学号从小到大分行输出学号，每行一个。
输入样例：
8 I
2101001 90 90 85 90 80 80
2101002 95 96 82 90 85 83
2101003 90 95 85 90 80 82
2101004 90 89 90 90 70 80
2102001 90 95 80 90 82 70
2102004 90 90 80 90 77 80
2102002 90 89 80 90 80 83
2102003 90 90 80 90 79 80
输出样例：语文、数学、物理、化学、政治、历史
2101003
'''
# 解题核心list_dict = [{} for i in range(100)] 字典列表
# n,m = input().split()
# n = int(n)
# print(n)
# list_dict = [{} for i in range(100)]
# for i in range(n):
#     list_dict[i]['xh'],list_dict[i]['yw'],list_dict[i]['sx'],list_dict[i]['wl'],list_dict[i]['hx'],list_dict[i]['zz'],list_dict[i]['ls'] = map(int,input().split())
#     print(list_dict[i])
#     print(i)
# r_list= []
# print(m)
# if m == 'I':
#     for i  in range(n):
#        r_list.append(list_dict[i]['sx']+list_dict[i]['wl'])
# r = max(r_list)
# print(r)
# for i  in range(n):
#     if list_dict[i]['sx']+list_dict[i]['wl']==r:
#         print(list_dict[i]['xh'])

'''
3. 合并检测
即将从k 个采集的标本放到同一个试剂盒中进行检测。
如果结果为阴性，则说明这 k 个人都是阴性，用一个试剂盒完成了 k 个人的检测。
如果结果为阳性，则说明至少有一个人为阳性，
需要将这 k 个人的样本全部重新独立检测
从理论上看， 如果检测前 k−1 个人都是阴性可以推断出第 k 个人是阳性，但是在实际操作中 不会利用此推断，而是将 k 个人独立检测），
加上最开始的合并检测，一共使用 了 k + 1 个试剂盒完成了 k 个人的检测。
估计被测的民众的感染率大概是 1%，呈均匀分布。请问 k 取多少能最节省试剂盒？
'''
# 取人数为100
# n = int(input())
# min = 9999999999
# res = 0
# for k in range(1,n+1):
#     c = (100-k)/k + (k+1)
#     if c <min:
#         min = c
#         res = k
# print(res)
'''
4.矩阵转置
给定一个n×m矩阵相乘，求它的转置。其中1≤n≤20，1≤m≤20，矩阵中的每个元素都在整数类型（4字节）的表示范围内。
输入格式
第一行两个整数n和m；
第二行起，每行m个整数，共n行，表示n×m的矩阵。数据之间都用一个空格分隔。
输出格式
共m行，每行n个整数，数据间用一个空格分隔，表示转置后的矩阵。
'''
# list_o= []
# m, n = map(int, input().split())
"""
构造矩阵列表
"""
# for i in range(0, m):
#     list_o.append(list(map(int, input().split())))
# print(list_o)
# import numpy as np
# list_o = np.array(list_o)
# print(list_o.T)
'''
一根高筋拉面，中间切一刀，可以得到2根面条。
如果先对折1次，中间切一刀，可以得到3根面条。
如果连续对折2次，中间切一刀，可以得到5根面条。 那么，连续对折10次，中间切一刀，会得到多少面条呢？
'''
# n = int(input())
# print(2 ** n + 1)
'''
给定 L, R，问 L ≤ x ≤ R 中有多少个数 x 满足存在整数 y,z 使得 x = y2 − z2。'''
# l,r = map(int,input().split())
# count = 0
# for t in range(l,r+1):
#      for i in range(round(t**(1/2)),round(t**(1/2))*2+1):
#          for j in range(0,round(t**(1/2))+1):
#               if t == i**2 - j**2:
#                   count+=1
#                   # print(f"{t}={i}**2-{j}**2")
# print(count)
from math import isqrt

def count_numbers(L, R):
    count = 0
    for x in range(L, R+1):
        factors = 0
        for i in range(1, isqrt(x)+1):
            if x % i == 0:
                factors += 2
        if isqrt(x)**2 == x:
            factors -= 1
        if factors % 2 == 0:
            count += 1
    return count

L = int(input("请输入 L 的值："))
R = int(input("请输入 R 的值："))
count = count_numbers(L, R)
print("满足条件的数的个数为：", count)
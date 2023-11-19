# 1.模拟报数游戏，n个人围成一圈从第一个人开始从1到k报数，报到k的人退出，圈子缩小，从一个人继续游戏，问最后留下的所原来的几号
# 给定两个字符串 text1 和text2 ，返回最长公共子序列长度
# text1,text2 = input().split(',')
# new_strlist = []
# index = -1
# for i in range(len(text1)):
#     for j in range(len(text2)):
#        if text1[i] == text2[j] and j > index:
#            new_strlist.append(text1[i])
#            # print(new_strlist)
#            # print(index)
#            index = j
#            # print(index)
#            break
# if new_strlist == None:
#     print("0")
# else:
#     print(len(new_strlist))



# 2.
# 小明决定购买一台价值5000元的电脑。
# 他决定从周一 开始每天放学后在学校的一家打印店进行勤工俭学，每天工作两个小时，每日可收入80元。
# 为了尽快购买电脑，他缩减了各项不必要的开支，每周日向饭卡中充值220元，且每21天需要支付话费80元，不考虑其它的额外花费，请问最快多少天后，才可以购买电脑？
# 本题无输入，输出格式：经过XX天，小明存到了****.**元钱，可以购买电脑。（说明：XX为整数形式，****.**为保留2位小数形式。）
sum1 = 5000 # 5000元的电脑
sal_day = 80 # 每日工资80元
# n*80 - n/7 *220 - n/21*80 >= 5000
for i in range(1,360):
    rmb = i*80 - i/7 *220 - i/21*80
    if rmb >= 5000:
        print("经过{}天，小明存到了{:.2f}元钱，可以购买电脑。".format(i,rmb))
        break




# 3.
# 快递行业的兴起慢慢的改变了人们的生活方式，越来越多的人选择了快递的方式。
# 列表LA和列表LB中分别存放了一位快递小哥今年9月份每天送件的单数和行车里程（公里）数，其中数值-1表示该天休息，并未送件。
LA=[90,114,-1,110,178,115,164,155,132,-1,174,153,124,189,110,145,-1,160,180,139,127,129,134,-1,160,178,150,144,145,-1]
LB=[87,163,-1,160,184,155,169,140,129,-1,190,156,141,200,115,150,-1,181,190,147,120,110,120,-1,170,167,144,135,110,-1]
# 要求：计算并输出9月份该快递小哥出工日每天平均的送件单数和平均的行车里程数，结果保留2位小数。
# 本题为唯一答案，没有输入参数,输出格式：平均每天送件单数：***.**,平均每天行车里程数：***.**（说明，输出字符串，精度为两位小数）
lc = list(i for i in LA if i != -1)
ld = list(i for i in LB if i != -1)
mean_num =  sum(lc)/len(lc)
men_m = sum(ld)/len(ld)
print('平均每天送件单数：{:.2f},平均每天行车里程数：{:.2f}'.format(mean_num,men_m))





# 4.
# 利用Python自带的turtle库完成如下图形的绘制。
# <font face="仿宋">绘图建议参考：右边正方形中最小的正方形的边长可设置为20，后面依次增加20.左边圆形最小圆形的半径可设置为10，后面依次增加10.</font></p>
import turtle
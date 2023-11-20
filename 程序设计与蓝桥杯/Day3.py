# 有六门功课（语文、数学、物理、化学、政治、历史）的成绩，现在需要从中选拔优秀同学参加如下学科竞赛：
# 生物竞赛（B）选拔化学和数学总分最高的同学，信息学竞赛（I）选拔物理和数学总分最高的同学，党史竞赛（H）选拔政治和历史总分最高的同学，
# 现在给出N名同学的各科成绩，请编写程序帮忙选出适合参加相应竞赛的同学。
# 输入说明：
# 第一行包括一个整数N和一个字符C，N表示参与选拔的同学人数，C表示选择的竞赛类型。
# 输出说明：
# 适合指定竞赛类型的学生学号。如果有多个符合条件的学生，按学号从小到大分行输出学号，每行一个。
# 输入样例：
# 8  I
# 2101001 90 90 85 90 80 80
# 2101002 95 96 82 90 85 83
# 2101003 90 95 85 90 80 82
# 2101004 90 89 90 90 70 80
# 2102001 90 95 80 90 82 70
# 2102004 90 90 80 90 77 80
# 2102002 90 89 80 90 80 83
# 2102003 90 90 80 90 79 80
# 输出样例：语文、数学、物理、化学、政治、历史
# 2101003

N, C= map(str,input().split()) # 输入n个数 与类别
N = int(N)
listGrades = []  #存数据
for i in range(N):
    tmp = input()
    listGrades.append((tmp.split()[0], tmp.split()[1], tmp.split()[2], tmp.split()[3], tmp.split()[4], tmp.split()[5], tmp.split()[6]))
    # [('2101001', '90', '90', '85', '90', '80', '80')] append 是这样一个元组
pointList = []
for i in listGrades:
    if C == "B":
        pointList.append((i[0],int(i[2])+int(i[4]))) # 如果为B 则将全部存入结果pointList，倒序，输出第一个则所最大的
    elif C == "I":
        pointList.append((i[0],int(i[1])+int(i[2])))
    elif C == "H":
        pointList.append((i[0],int(i[5])+int(i[6])))
pointList.sort(key=lambda x:x[1],reverse=True)
for i in pointList:
    print(i[0], end='  ')

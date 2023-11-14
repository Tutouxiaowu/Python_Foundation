# 什么是数据结构
# 即是，数据存储的结构方式，常见的有，数组，队列，堆栈，列表，树，图
# 什么是算法呢
# 让数据结构跑起来的就是算法

# 时间复杂度 ： Tn = O(1) O(LOG N ) < O(N) < O(OLOG N) < O(N^2)
# 特别注意的点是 ：O LOGN

def cal(n):
    sum = 1
    time =0
    while sum <n:
        sum = sum*2
        time += 1
    return time
print(cal(100))
# logn 类似的，n起手，但是所需要的时间（或者说处理的次数）不为 n，而是对半折中的x
# 像这样吧这函数执行n遍
def cal(n):
    # 故而 这样的函数，复杂度为nlogn
    for i in range(n):
        sum = 1

        while(sum < n):
            sum = sum * 2
# 在我们观察复杂度的时候，通常只观察最复杂的代码
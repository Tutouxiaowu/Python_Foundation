### 异常
try:
    x = 1/0
except ZeroDivisionError as err: # 当此类异常发生时，捕获异常，并执行一下内容
    print(f'程序发生异常，错误信息：{err}')
# 但是因为我提前不知道，我此代码到底会出现哪一种异常 所以我可以多写几种，当捕获到相应异常时，才可以被执行
except IndexError as err:
    print(f'这个异常可以忽略')
# 当然 当我不知道具体会发生什么异常的时候 也可以这样 ：
try:
    x = 1/0
except Exception as err: # 因为Exception 是超类
    print(f'程序发生异常，异常信息：{err}')

try:
    with open("caoxiaohua.txt")as f:
        f.read()
except FileNotFoundError as err:
    print("文件不存在",err)
else:
    print("打开文件操作没毛病，继续你的操作")
finally:
    print("一定会干的事情")
"""
多行注释：自定义异常
"""

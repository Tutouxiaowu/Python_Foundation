import random
from matplotlib import pyplot as plt
# 1.
# >>的意思是将二进制左移3位（变小）
print(211>>3)
print(21<<3)

# 2.
# eval():简单来说就是将字符串转换为python代码执行 此外eval()可以生产动态方法，类等(动态生成代码、实现动态配置、实现动态计算)
print(eval('1+2'))
# func_name = "addition"
# func_str = "def " + func_name + "(x, y):\n return x + y"
# eval(func_str)
# result = addition(1, 2)
# print(result)
# 创建子图需要注意的是，(int,int,index)->233其实就是(2,3,3) 所以不能plt.subplot(1028)
plt.subplot(223)

# 3. 一维数据可以采用特殊符号@分隔方式存储

# 4. 利用random.uniform(10,20)语句，可生成一个[10,20]之间的随机小数
n = random.uniform(10,20)
print(n)

# 5. python常用的标准库有 random,datetimes,re,sys等等


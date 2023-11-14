## format格式化
# 通常我们知道格式化输出
print("{}尊的是{}".format("gyn",18.00000))
name = 'gyn'
age = 18.000
print(f'{name}尊的是{age}')
# 如果我要将 18.000 改为整形，或者两位小数呢
print("{}尊的是{:.2f}".format("gyn",18.00000)) # 保留2位
print("{}尊的是{:.0f}".format("gyn",18.00000)) # 整型
# 指定进制
# 指定百分比
value = 0.25
percentage = "{:.2%}".format(value)
print(percentage)
# 科学计数法表示
value = 12345.6789
scientific = "{:.2e}".format(value) #2e 保留两位小数
print(scientific)
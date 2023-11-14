
# my_list = list(input().split(","))
# for i in range(len(my_list)):
#     my_list[i] = float(my_list[i])
# sum = 0
# for i in my_list:
#     sum = i + sum
# mean = sum / len(my_list)
# print("{:.2f}".format(mean))

str = input("请输入以个小写字母串:")
ascii_list = []
for char in str:
    ascii_list.append(ord(char))
    print(ascii_list)
ascii_list.sort()
new_str = ""
for ascii_code in ascii_list:
    new_str += chr(ascii_code)
print(f"从小到大排列为{new_str}")

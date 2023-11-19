# 首先基本格式：
'''
# 导入turtle
import turtle

# (--------中间写绘图过程----------)

# 让画布一直存在，这句代码需要放在最后
turtle.mainloop()
'''
import turtle
turtle.setup(800, 600)
turtle.title('hello')
# 画笔设置
turtle.pencolor('red')
turtle.width(4)
turtle.speed(4)
# 控制笔的移动

# 画正方形
turtle.up()
turtle.goto(-20,150)
turtle.down()
turtle.goto(-320,150)
turtle.goto(-320,-150)
turtle.goto(-20,-150)
turtle.goto(-20,150)

# 画圆形
turtle.up()
turtle.goto(170,-150)
turtle.down()
turtle.circle(150)

# 画文字
turtle.write("我真帅",font=(40))

# 填充颜色
# turtle.fillcolor(颜色) - 设置填充颜色
# turtle.begin_fill() - 开始填充
# turtle.end_fill() - 结束填充

turtle.mainloop() # 保持画布
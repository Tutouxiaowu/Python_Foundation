# python中的面向对象是和java相似的
# 类——即结构体
class Person:
   style = 'i人' # 共有变量，都有的变量
   def __init__(self,name,age): #构造方法初始化——>构造方法只能有一个
       self.name = name
       self.age = age
   #  OK 定义了这个人，他会干嘛，他拿来干嘛的
   def say(self):
       print('caoxiaohua：我尊嘟栓q')
   def play(self):
       print("timing,我爱玩王者荣耀")
caoxiaohua = Person('CAOXIAOHUA','19')
print(caoxiaohua.name)
print(caoxiaohua.age)
print(caoxiaohua.style)
caoxiaohua.say()
class YellowPeople(Person): # 继承于person
    # def __init__(self,name,age):
    #     super.__init__(self,name,age) #
        #Person.__init__(self,name,age)
    def say(self):
        print('吴超，我是真滴帅')
# 此时 yellowpeople可以调用其构造方法和其他方法
wuchao = YellowPeople('WUCHAO',20)
print(wuchao.age)
print(wuchao.name)
wuchao.say()
#### 对象多继承（java是不支持多继承的，因为会很复杂，但是java提供接口，以解决多继承的问题）
class PersonFather(Person):
    def say(self):
        print("父类：曹小华666")
class PersonMother(Person):
    def say(self):
        print("Mother》曹小华66666")
class caoxiaohua(PersonMother,PersonFather): #当方法相同时，先调用前面的，最后调用的是爷类
    pass
caohua = caoxiaohua('c',19)
caohua.say()

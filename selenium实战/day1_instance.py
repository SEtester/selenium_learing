#encoding:utf8

class Human():
    name = 'XXX'

    def __init__(self,name):
        # 优先调用实例属性
        self.name = name



person1 = Human('杨芳振')
print(person1.name)
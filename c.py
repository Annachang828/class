# class 類別(種類)

class Student:
    def __init__(self, name, score): # intitialize 初始化
        self.name = name
        self.score = score
        print('我誕生了!')

    def do_hw(self, hw):
        print('我在做作業', hw)

    def study(self):
        print('我在讀書')
        self.score += 5

    def sleep(self):
        print('shh, I am sleeping')

s1 = Student('Anna', 100)
s2 = Student('John', 60)
print(s1.name,s1.score)
print(s2.name,s2.score)

s2.study()
print(s2.name, s2.score)
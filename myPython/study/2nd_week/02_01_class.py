class Person:
    def __init__(self, name_param):
        self.name = name_param
        # print("hihi i am created", self, self.name)
    
    def talk(self):
        print("안녕하세요 저는", self.name, "입니다")

# 아래의 Person() '생성자 함수' 
# '생성자 함수'란 클래스를 이용하여 객체를 만들 때 필요한 함수
person1 = Person('유재석')
person1.talk()

person2 = Person('박명수')
person2.talk()
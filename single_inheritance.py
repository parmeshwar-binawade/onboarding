class parent_class:
    # b = a = none
    a=b=0
    def __int__(self):
        print("This is parent class")

    def calculate(self):
        print("Parent class calculate method")
        return self.a + self.b


class child_class(parent_class):
    a2=b2=0
    def __int__(self):
        print("This is child class")

    def __init__(self,a,b):
        self.a2=a
        self.b2=b
        self.a=a
        self.b=b

    def calculate(self):
        print("Child class calculate method")
        self.a2=super().calculate()
        return self.a2 + self.b2

    def calculate2(self):
        #         check instance variable updated value(a)
        print("Calculate2 method called")
        return self.a

obj = child_class(3,4)
result = obj.calculate()
print(result)
result2=obj.calculate2()
print(result2)


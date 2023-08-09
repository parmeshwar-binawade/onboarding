class A:
    def __init__(self):
        print("class A constructor")

class B(A):
    def __init__(self):
        print("Class B constructor")
        super().__init__()

class C(A):
    def __init__(self):
        print("Class C constructor")
        super().__init__()

obj=C()
obj2=B()

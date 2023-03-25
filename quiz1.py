class A:

    def __init__(self):

        self.a = 100

 

class B:

    def __init__(self):

        self.b = 200

        

        

class C(B, A):

    def __init__(self):

        super().__init__()

    def method_1(self):

        print(self.b)

        

    

c = C()

c.method_1()
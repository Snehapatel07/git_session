class Parent:
    def __init__(self):
        super().__init__()
        print("in parent __init__")
        self.game = "Cricket"
class Base1(Parent):
    def __init__(self):
        super().__init__()
        print("in Base 1 __init__")
        self.name = "Kapil Dev"
        
class Base2(Parent):
    def __init__(self):
        super().__init__()
        print("in Base 2 __init__")
        self.occupation = "Player"
    def display(self):
        print("in Base2 class")
        
class Base3(Parent):
    def __init__(self):
        self.best_score = 170
        super().__init__()
        print("in Base 3 __init__")
    def display(self):
        print("in a Base 3 class")
        
class Child(Base1, Base2, Base3):
    def __init__(self):
        super().__init__()
    
child = Child()
print(child.__dict__)
print(Child.__mro__)
child.display()

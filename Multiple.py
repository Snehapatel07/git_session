class Base1:
    def __init__(self):
        self.name = "Kapil Dev"
        
class Base2:
    def __init__(self):
        self.occupation = "Player"
    def display(self):
        print("in Base2 class")
        
class Base3:
    def __init__(self):
        self.best_score = 170
    def display(self):
        print("in a Base 3 class")
        
class Child(Base1, Base2, Base3):
    pass
child = Child()
child.display()

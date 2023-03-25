class BaseClass:
    def __init__(self,new_value):
      self.name = new_value
  
    def get_name(self):
        return self.name
class Child(BaseClass):
    def __init__(self, new_value):
        # Base Constructor, needs Explicit call
        #super(). __init__(new_value)
        pass
first_child = Child("Gaurav")
print(first_child.get_name())
#print(first_child.name)
#print(first_child. __dict__)

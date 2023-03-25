class Test:
    def __init__(self,val):
        self.__val = val #private
# getter method.function name same as attribute name 
    @property
    def val(self):
        return self. __val
#setter method.function name same as attribute name
    @val.setter
    def val(self,new_val): #private
        if new_val>100:
            self. __val=100
        else:
            self. __val = new_val
   
obj1= Test(3)
print(obj1.val)
obj1.val = 99
print(obj1.val)
obj1.val = 20
print(obj1.val)
    
            
        
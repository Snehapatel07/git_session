class ABC:

    def __init__(self):

        self.__count = 5

    

    @property    

    def count(self):

        return self.__count

 

    @count.setter    

    def count(self, count):

         self.__count = count

    

abc = ABC()
abc.count = 23

print(abc.count)

class Measure:
    def__init__(self):
        self.measure = 0
@Staticmethod
def convert_inch_to_cm(inches):
    print(inches*2.54)
def convert_cm_to_inches(cms):
    print(cms 2.54)
    
Measure.convert_cm_to_inches=staticmethod(Measure.convert_cm_to_inches)
obj=Measure()
obj.convert_inch_to_cm(10)
Measure.convert_inch_cm(10)
obj.conert_cm_to_inches(25.4)
Measure.convert_cm_to_inches(25.4)
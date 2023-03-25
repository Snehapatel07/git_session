from abc import ABC,abstractmethod

class Switch(ABC):
    @abstractmethod
    def switch_on():
        pass
    @abstractmethod
    def switch_off():
        pass
class PlasticSwitch(Switch):
        def switch_on():
            print("Switch on")
            
        def switch_off():
            print("Switch off")
class WifiSwitch(Switch):
        def switch_on():
            print("Switch on")
        
        def switch_off():
            print("switch off")
            
        
        
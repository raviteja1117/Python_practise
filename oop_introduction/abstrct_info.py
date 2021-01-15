
from abc import ABC, abstractmethod

class Laborotory_Guidelines(ABC):
    @abstractmethod
    def temparature_protection(self):
        pass
    @abstractmethod
    def explosives_protection(self):
        pass

class Sugar_Facory(Laborotory_Guidelines):
    def temparature_protection(self):
        print("temparature_protection implemented...")
    def explosives_protection(self):
        pass

factory = Sugar_Facory()
factory.temparature_protection()
factory.explosives_protection()

# we can't create an instance for an abstract class
lab=Laborotory_Guidelines()
from abc import ABC,abstractmethod
class AbsClass(ABC):
    @abstractmethod
    def abs_method(self):
        pass
class ConcreteClass(AbsClass):
    def abs_method(self):
        n = 1000
        print("abstrace method defined: ",n)

obj = ConcreteClass()
obj.abs_method()
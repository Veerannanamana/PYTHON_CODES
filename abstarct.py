from abc import ABC,abstractmethod
class vechile(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class bike(vechile):
    def start(self):
        print("Bike is start")
    def stop(self):
        print("Bike is stop")
class car(vechile):
    def start(self):
        print("car is start")
    def stop(self):
        print("Bike is stop")
b=bike()
b.start()
c=car()
c.start()
b.stop()
c.stop()

from abc import ABC, abstractmethod
#abc- abstract base class
class Bike(ABC):
    @abstractmethod
    def run(self):
        pass

class Pulsar(Bike):
    def run(self):
        print("pulsar")

class KTM(Bike) :
    def run(self):
        print("KTM")

if __name__ == '__main__':
    # b = Bike() # error - Can't instantiate abstract class Bike with abstract methods
    p = Pulsar()
    k = KTM()
    p.run()
    k.run()
i
# class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# method
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

h1 = Human("John", 36)
h1.myfunc()

# encapsulation
class Rekening:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

rekening = Rekening(1000)
print(rekening.get_saldo())

# inheritance
class Kendaraan:
    def __init__(self, nama):
        self.nama = nama

    def berjalan(self):
        print(self.nama + " sedang berjalan")
        
class Mobil(Kendaraan):
    def meong(self):
        print(self.nama + " sedang mengeong")

k = Mobil("Kucing")
k.berjalan()
k.meong()

# polymorphism
class Panda:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama + " sedang makan")

class Orang:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama + " sedang makan")

panda = Panda("Panda")
orang = Orang("Orang")

for hewan in (panda, orang):
    hewan.makan()

# abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def berjalan(self):
        pass
    
class Car(Kendaraan):
    def berjalan(self):
        print("Mobil berjalan")

car = Car("Mobil")
car.berjalan()



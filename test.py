import json, requests, uuid
from abc import ABC, abstractclassmethod, abstractmethod

class User:
    def __init__(self, first= None, last= None, age=None):
        if first is not None and last is not None and age is not None:
            if isinstance(first, str) and isinstance(last, str) and isinstance(age, int):
                self.first = first
                self.last = last
                self.age = age
            else:
                raise ValueError("Invalid data types: first and last must be strings, age must be an integer.")
        else:
            raise ValueError("None values are not allowed for first, last, or age.")

    @classmethod
    def create(cls, validate_date):
        user = User(**validate_date)
        malumotlar = []
        with open('malumotlar.json', 'a') as f:
            malumotlar.append(user.__dict__)
            f.write(',\n')
            json.dump(malumotlar, f, indent=4)
    
    
h = [12, 32, 32]
d = {'first': 'sardor', 'last':'sda', 'age':32}





class Dokon:
    def __init__(self, product, order) -> None:
        self.product = product
        self.order = order

    def __str__(self) -> str:
        pr =  self.__dict__['product']
        pr2 = self.product
        print(pr2)
        return pr

d = Dokon('telefon', 'buyurtma')
print(d)





class colore:
    def __init__(self, start, end):
        if isinstance(start,int) and isinstance(end,int):
            self.start = start
            self.end = end
    
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == self.end:
            raise StopIteration
        result = self.start + self.index
        self.index += 1
        return result
colore = colore
for i in colore(-1,67):
    print(i)




def test(a,b,c):
    return a, b, c

dik = {'a':4, 'b':6, 'c':9}
lis = [('a', 4), ('b', 6), ('c', 9)]
qw = 1, 2, 2
print(test(**dik))
print(test(*lis))
print(test(*qw))


print(((10 * 53) + (6.25 * 171) - (5* 17) + 5) * 1.4)
print(53 / (1.71 * 1.71))


class Car(ABC):
    def __init__(self, model, year, color, motor, kmh, benzin, price):
        self.model = model
        self.year = year
        self.color = color
        self.motor = motor
        self.speed = kmh
        self.benzin = benzin
        self.narx = price
        self.__id = uuid.uuid4()

    def __str__(self):
        return (f"Model: {self.model}\n"
                f"year: {self.year}\n"
                f"color: {self.color}\n"
                f"Motor: {self.motor}\n"
                f"kmh: {self.speed} km/p\n")

    @abstractmethod
    def get_mph(self):
        tez = int(input(
            f'kiriting shu kirtilgan soniya ichida {self.model} nech metr yol bosib otilishini hisoblanadi: '))
        if isinstance(tez, int):
            tezlik = self.speed * 10
            natija = tezlik * tez // 36
            return f'{self.model} {tez} soniyada {natija} metr bosib otadi'
        return None

    @abstractmethod
    def get_kmh(self):
        soni = int(input(f'kiriting shu kiritilgan soat ichida {self.model} qancha yol bosib otishini hisoblanadi: '))
        if isinstance(soni, int):
            natija = self.speed * soni
            return f'{self.model} {soni} soatda {natija} km yol bosib otadi'
        return None

    @abstractmethod
    def get_id(self, password):
        self.password = 5432
        if self.password == password:
            return f'sizning id: {self.__id}'
        return None


class Bmw(Car):
    def __init__(self, model, year, color, motor, kmh, benzin, price):
        super().__init__(model, year, color, motor, kmh, benzin, price)
    
    def get_mph(self):
        return super().get_mph()
    
    def get_kmh(self):
        return super().get_kmh()
    
    def get_id(self, password):
        return super().get_id(password)
    
bmw = Bmw('m5 f90', 2021, 'red', 'twin turbo', 310, 'ai95', 200000)


class Toyota(Car):
    def __init__(self, model, year, color, motor, kmh, benzin, price):
        super().__init__(model, year, color, motor, kmh, benzin, price)
    
    def get_mph(self):
        return super().get_mph()
    
    def get_kmh(self):
        return super().get_kmh()
    
    def get_id(self, password):
        return super().get_id(password)

supra = Toyota('SUPRA MK4', '2001', 'qizil','twin-turbo 3.0-litre straight six', 349, 'ai96', 420000)











x = 7
y = 8 -2 *2

cos = (x / y) + 12 / (6)
print(cos)
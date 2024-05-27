class Car:

    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    # defining object behaviour through methods
    def speed(self):
        print(f'{self.name} is speeding')
    def mileage(self):
        print(f'{self.name} has a mileage of 13.47 kmpl')
    def fuel_capacity(self):
        print(f'{self.name} has a fuel capacity of 70 litres')

# creating an object by creating class instance
Audi = Car("Audi", "Q7")

print(Audi.name)
print(Audi.speed())
print(Audi.mileage())
print(Audi.fuel_capacity())


# create a class of a car. add any attributes. add 2-3 methods that describes the car

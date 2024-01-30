class Vehicle:
    def __init__(self, brand, model, speed, fuel_type):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.fuel_type = fuel_type

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} {self.model} is accelerating. Current speed: {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        print(f"{self.brand} {self.model} is braking. Current speed: {self.speed} km/h")

    def refuel(self):
        print(f"{self.brand} {self.model} is refueling.")


class Car(Vehicle):
    def __init__(self, brand, model, speed, fuel_type, number_of_wheels):
        super().__init__(brand, model, speed, fuel_type)
        self.number_of_wheels = number_of_wheels

    def honk(self):
        print(f"{self.brand} {self.model} is honking.")


class Airplane(Vehicle):
    def __init__(self, brand, model, speed, fuel_type, number_of_engines, has_landing_gear):
        super().__init__(brand, model, speed, fuel_type)
        self.number_of_engines = number_of_engines
        self.has_landing_gear = has_landing_gear

    def take_off(self):
        print(f"{self.brand} {self.model} is taking off.")


my_car = Car('Toyota', 'Corolla', 0, 'Petrol', 4)
my_airplane = Airplane('Boeing', '747', 0, 'Jet Fuel', 4, True)

my_car.accelerate()
my_car.brake()
my_car.refuel()
my_car.honk()

my_airplane.accelerate()
my_airplane.brake()
my_airplane.refuel()
my_airplane.take_off()

class Vehicle:
    def __init__(self, make, model, year, miles):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles

    def mileage(self):
        pass

    def print_details(self):
        print(self.make + ' ' + self.model + ' was produced in year ' + str(self.year) + '.')


class Car(Vehicle):
    def __init__(self, make, model, year, miles):
        super().__init__(make, model, year, miles)

    def mileage(self):
        return self.miles / 0.75

    def towing_capacity(self):
        return self.miles * 50

    def print_details(self):
        super().print_details()
        print('It has mileage ' + str(self.mileage()) + ' and towing capacity ' + str(self.towing_capacity()) + '.')


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, miles):
        super().__init__(make, model, year, miles)

    def mileage(self):
        return self.miles / 0.75

    def print_details(self):
        super().print_details()
        print('It has mileage ' + str(self.mileage()) + '.')


class Truck(Vehicle):
    def __init__(self, make, model, year, miles):
        super().__init__(make, model, year, miles)

    def mileage(self):
        return self.miles / 0.45

    def towing_capacity(self):
        return self.miles * 100

    def print_details(self):
        super().print_details()
        print('It has mileage ' + str(self.mileage()) + ' and towing capacity ' + str(self.towing_capacity()) + '.')


car = Car('Dacia', 'Spring', 2022,765)
truck = Truck('Beryl', 'M14', 2019,90)
moto = Motorcycle('MK14','Autoh',2023, 123)

car.print_details()
truck.print_details()
moto.print_details()
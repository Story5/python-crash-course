from car import Car
from battery import Battery 
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a " + str(self.battery.battery_size) + "-kWh battery.")
    def fill_gas_tank(self):
        print('This car has no gas.')

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
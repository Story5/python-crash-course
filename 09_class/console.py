import car

my_car = car.Car('audi','a4',2016)
print(my_car.make)
print(my_car.model)
print(my_car.year)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.odometer_reading = 23
my_car.read_odometer()

my_car.update_odometer(30)
my_car.read_odometer()

my_car.increment_odometer(10)
my_car.read_odometer()
my_car.fill_gas_tank()
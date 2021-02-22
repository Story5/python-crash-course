class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        """默认值"""
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + " miles on it")

    def fill_gas_tank(self):
        print('Car has gas')
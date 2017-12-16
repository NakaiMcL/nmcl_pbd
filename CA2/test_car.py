import unittest

from car import Car, CarFleet, ElectricCar, PetrolCar, DieselCar, HybridCar

# test the car functionality
class TestCar(unittest.TestCase):

    def test_car_mileage(self):
        self.car = Car()
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.setMileage(45)
        self.assertEqual(45, self.car.getMileage())

    def test_car_make(self):
        self.car = Car()
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.car = Car()
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        self.car.setColour('yellow')
        self.assertEqual('yellow', self.car.getColour())

    def test_electric_car_fuel_cells(self):
		electric_car = ElectricCar()
		self.assertEqual(1, electric_car.getNumberFuelCells())
		electric_car.setNumberFuelCells(4)
		self.assertEqual(4, electric_car.getNumberFuelCells())

    def test_diesel_car_cylinders(self):
		diesel_car = DieselCar()
		self.assertEqual(1, diesel_car.getNumberCylinders())
		diesel_car.setNumberCylinders(4)
		self.assertEqual(4, diesel_car.getNumberCyclinders())

    def test_hybrid_car_fuel_cells(self):
		hybrid_car = HybridCar()
		self.assertEqual(1, hybrid_car.getNumberFuelCells())
		hybrid_car.setNumberFuelCells(4)
		self.assertEqual(4, hybrid_car.getNumberFuelCells())

    def test_petrol_car_cyclinders(self):
		petrol_car = PetrolCar()
		self.assertEqual(1, petrol_car.getNumberCylinders())
		petrol_car.setNumberCylinders(4)
		self.assertEqual(4, petrol_car.getNumbeCylinders())

    def test_car_fleet(self):
        car_fleet = CarFleet()
        self.assertEqual(0, car_fleet.getProfit())
        self.assertEqual(40, car_fleet.getNumAvailable())


        car_fleet.rentCar(5)
        self.assertEqual(100, car_fleet.getProfit())
        self.assertEqual(35, car_fleet.getNumAvailable())


        car_fleet.returnCar(2)
        self.assertEqual(37, car_fleet.getNumAvailable())


        car_fleet.returnCar(3)
        self.assertEqual(40, car_fleet.getNumAvailable())

        car_fleet.returnCar(3)
        car_fleet.rentCar(50)

if __name__ == '__main__':
    unittest.main()

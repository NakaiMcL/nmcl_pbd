# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0
        self.__regNo = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model
        
    def getMileage(self):
        return self.__mileage
        
    def getRegNo(self):
        return self.__regNo

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make
        
    def setModel(self, model):
        self.__model = model

    def setMileage(self, mileage):
        self.__mileage = mileage
        
    def setRegNo(self, regNo):
        self.__regNo = regNo

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 8

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells
        
class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 8

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

class CarFleet(object):

    def __init__(self):
        self.__cars = []
        self.__numAvailable = 40
        self.__profit = 0.0

    def getProfit(self):
        return self.__profit

    def getNumAvailable(self):
        return self.__numAvailable

    def rentCar(self, numCars):
        self.__numAvailable -= numCars
        self.__profit += (numCars * 20)
        print('Profit ' + str(self.__profit))
        print('Available ' + str(self.__numAvailable))

    def returnCar(self, numCars):
        self.__numAvailable += numCars
        print('Available ' + str(self.__numAvailable))
        
         
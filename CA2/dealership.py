
from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

class Dealership(object):

    def __init__(self):
        self.ElectricCar = []
        self.PetrolCar = []
        self.DieselCar = []
        self.HybridCar = []

    def create_current_stock(self): #Number of cars at the beginning
        for i in range(10):
           self.ElectricCar.append(ElectricCar())
        for i in range(10):
           self.PetrolCar.append(PetrolCar())
        for i in range(10):
           self.DieselCar.append(DieselCar())
        for i in range(10):
           self.HybridCar.append(HybridCar())

    def stock_count(self): #Cars available
        print 'petrol cars in stock ' + str(len(self.PetrolCar))
        print 'electric cars in stock ' + str(len(self.ElectricCar))
        print 'diesel cars in stock ' + str(len(self.DieselCar))
        print 'hybrid cars in stock ' + str(len(self.HybridCar))

    def process_rental(self): #customer's choice of car
        answer1 = raw_input('Welcome to Angier Car Rental. Would you like to rent a car? y/n')
        if answer1 == 'y':
            answer2 = raw_input('What type would you like? Click p for a Petrol car, d for Diesel, e for Electric or h for Hybrid')
            amount = int(raw_input('How many would you like?'))
            if answer2 == 'p':
                self.rent(self.PetrolCar, amount)
            elif answer2 == 'd':
                self.rent(self.DieselCar, amount)
            elif answer2 == 'e':
                self.rent(self.ElectricCar, amount)
            elif answer2 == 'h':
                self.rent(self.HybridCar, amount)
            else:
            	print 'Try again. Please enter p, d, e or h'
        elif answer1 == 'n':
            print 'Thank you. If you need a car to rent in the future, Aungier Car Rental will be happy to help.'
        else:
        	print 'Try again. Please enter y/n'
        self.stock_count()

	def rent(self, PetrolCar, amount): #rent car 
		total = 0
		while total < amount:
			PetrolCar.pop()  
			total = total + 1
            
	def rent(self, ElectricCar, amount):
		total = 0
		while total < amount:
			ElectricCar.pop()  
			total = total + 1	
	
	def rent(self, DieselCar, amount):
		total = 0
		while total < amount:
			DieselCar.pop()  
			total = total + 1

    def rent(self, HybridCar, amount):
		total = 0
		while total < amount:
			HybridCar.pop()
			total = total + 1

    def rental_cars(self): #check if the car is available
    	if answer2 == 'p':
    		if len(self.PetrolCar) < amount:
    			print 'Petrol cars are out of stock. Please choose another option.'
    			return
    		else:
    			print 'Excellent choice! Enjoy your car'
    		self.rent(self.PetrolCar, amount)
    		self.stock_count

		elif answer2 == 'e':
    		if len(self.ElectricCar) < amount:
    			print 'Electric cars are out of stock. Please choose another option.'
    			return
    		else:
    			print 'Excellent choice! Enjoy your car'
    		self.rent(self.ElectricCar, amount)
    		self.stock_count

		elif answer2 == 'd':
    		if len(self.DieselCar) < amount:
    			print 'Diesel cars are out of stock. Please choose another option.'
    			return
    		else:
    			print 'Excellent choice! Enjoy your car'
    		self.rent(self.DieselCar, amount)
    		self.stock_count

		elif answer2 == 'h':
    		if len(self.HybridCar) < amount:
    			print 'Hybrid cars are out of stock. Please choose another option.'
    			return
    		else:
    			print 'Excellent choice! Enjoy your car'
    		self.rent(self.DieselCar, amount)
    		self.stock_count
            
# Return car -adds cars back to stock

    def returncar(self, PetrolCar, amount):
        total = 0
        while total < amount:
            PetrolCar.append(PetrolCar()) 
	    total = total + 1
            		
	def returncar(self, ElectricCar, amount):
		total = 0 
		while total < amount:
			ElectricCar.append(ElectricCar())
		total = total + 1
	
	def returncar(self, DieselCar, amount):
		total = 0
		while total < amount:
			DieselCar.append(DieselCar()) 
		total = total + 1
			
	def returncar(self, HybridCar, amount):
		total = 0
		while total < amount:
			HybridCar.append(HybridCar()) 
		total = total + 1      		

if __name__ == '__main__':
	dealership = Dealership()
	dealership.create_current_stock()
	proceed = raw_input('continue? y/n')
		if proceed == 'y':
    		dealership.process_rental()
		else:
			quit()

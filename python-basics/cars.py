#Name:Karen Mwaniki
#Date:23/02/2026
#program to show classes in python

class Car():
    #First we define the attributes of a car
    def __init__(self,model,make,color,year):
        self.model=model
        self.make=make
        self.color=color
        self.year=year
    
    #print the details of the car
    def print_details(self):
        print(f"Model: {self.model}, Make: {self.make} of Color: {self.color}, Year: {self.year}")



#instantiate a class object
my_car=Car("Audi","RS8","Sundust",2022)
dads_car=Car("Mercedes","AMG","Black",2020)


my_car.print_details()
dads_car.print_details()
#Name:Karen Mwaniki
#Date:23/02/2026
#program to inheritance in python

class Animal():
    def __init__(self, species, food, weight, age):
        self.species = species
        self.food=food
        self.weight=weight
        self.age=age

    def grow(self,weight):
        weight=1.1 * weight
        print(f"the animal weighs {weight}kgs")

    def eat(self,food):
        print(f"the animal eats {food}") 

class Dog(Animal):
    def __init__(self, species, food, weight, age):
        self.species = species
        self.food=food
        self.weight=weight
        self.age=age

    def grow(self,weight):
        weight=1.1 * weight
        print(f"the animal weighs {weight}kgs")

    def eat(self,food):
        print(f"the animal eats {food}") 


class Horse(Animal):
    def __init__(self, species, color, breed):
        super().__init__(species, "meat", 2)
        self.color=color
        self.breed=breed

    def grow(self,weight):
        weight=1.1 * weight
        print(f"the animal weighs {weight}kgs")

    def eat(self,food):
        print(f"the animal eats {food}") 

    def bark(self):
        print("the horse says neigh neigh")    
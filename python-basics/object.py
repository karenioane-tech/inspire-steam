#Name:Karen Mwaniki
#Date:19/02/2026
#program to show objects in python

class Human:
    #First we define the attributes of a human
    type="mammal"
    legs=2
    brain=True
    warm_blooded=True
    city="Nairobi"

#we then create a constructor for class objects
#The constructor will be used to create copies of the human class
    def __init__(self,name,age):
        self.human_name=name
        self.human_age=age

    def tell_story(self):
        print(f" Hello, I am {self.human_name} Here is a story.")
        print("There was a human named Karen and she was learning about objects in python. ")

#create the humans
Karen   = Human("Karen",17)
Saenyi= Human("Saenyi",30)

#let the humans create do things
Karen.tell_story()
print(f"Karen is: {Karen.human_age} years old.")

#modify one of the objects without modifying one of the objects
Saenyi.city="Mombasa"

print(f"Saenyi's location is {Saenyi.city}")
print(f"Karen's location is {Karen.city}")
      


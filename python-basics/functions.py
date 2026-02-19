#Name:Karen Mwaniki
#Date:19/02/2026
#program to show functions in Python

def cook_egg():
    oil="2 tablespoons"
    egg="2"
    pan=True
    fire="medium"
    
    print(f"the pan is {pan},the fire is {fire},add {oil} of oil and crack {egg} eggs into the pan")

print("here is statement 1 ")

print("here is statement 2")

cook_egg()

print("here is statement 3")

#bus fares creating function

def create_fare(route,distance, is_rush_hour):
    fare_distance=distance*10
    if is_rush_hour== True:
        fare= fare_distance*1.5
        print(f"the fare on route{route} is {fare}")

        return fare

rush_hour=True
returned_fare = create_fare("Juja-Allsops",7,rush_hour)
print(f"Returned fare is: {returned_fare}")

#passing a list as a parameter
def write_all_interests(interests):
    for interest in interests:
        print(f" I am interested in {interest}")

all_interests=["travelling","cooking","adrenaline activities"]

write_all_interests(all_interests)
              
              

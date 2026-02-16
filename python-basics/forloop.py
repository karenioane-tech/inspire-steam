#Name:Karen Mwaniki
#Date:13/02/2026
#program to show for loops in python
import math

for x in range(0,360,30):
    print(math.cos(x))

    for x in range(0,360,30):
        print(math.sin(x))

for x in range(0,360,30):
    print(math.tan(x))

    for i in range(10,0,-1):
        print(i)

        import math

        for k in range(-180,+180,30):
            print(math.cos(k))
            print(math.sin(k))
            print(math.tan(k))

            print("___________________________________________")
            print("|  k  |  _________________________________  |")
            print("|     |  cos(k)  |  sin(k)  |  tan(k)   |")


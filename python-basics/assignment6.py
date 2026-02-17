#Name:Karen Mwaniki
#Date:17/02/2026
#program to display diamond

#diamond
rows=int(input("enter the number of rows:"))

#top part of the diamond
for i in range(rows):
    spaces = ' ' * (rows - i - 1)
    stars= '*' * (2 * i + 1)
    print(spaces+stars)

#bottom part of the diamond
for i in range(rows-2, -1, -1):
    spaces = ' ' * (rows - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

 #triangle

rows=int(input("enter the number of rows: "))
for i in range(1,rows+1):
    print(" "*(rows-i)+"*"*(2*i-1))

#solving quadratic equation

#quadratic formula: ax^2+bx+c=0
 
import math
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

#calculate the discriminant
discriminant=b**2-4*a*c

if discriminant>0:
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    print(f"the roots are {root1} and {root2}")
elif discriminant==0:
    root=-b/(2*a)
    print(f"the root is {root}")
else:
    print("no real roots")
#Name:Karen Mwaniki
#Date:16/02/2026
#program to calculate factorials of numbers

number=int(input("enter the number x:")) #capture the number from the user
factorial=1 #initialize the  factorial 
for x in range(0,number):
    factorial=factorial*(x+1) 
    number=number-1
    print(f"{number}!={factorial}")
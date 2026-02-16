#Name:Karen Mwaniki
#Date: 13/02/2026
#This program calculates geometric progression

#calculating the nth term of a geometric progression

a=int(input("Enter the first term of the geometric progression: "))
r=int(input("Enter the common ratio of the geometric progression: "))
n=int(input("Enter the term number "))

nth_term=a*(r**(n-1))

print("The nth term of the geometric progression is: ", nth_term)

#calculating the sum of the first n terms of a geometric progression
if r==1:
    gp_sum=a*n
else:
    gp_sum=a*(1-r**n)/(1-r)

print("The sum of the first n terms of the geometric progression is: ", gp_sum)
#Name:Karen Mwaniki
#Date:13/02/2026
#Program to calculate arithmetic progression

#calculating the nth term

a=int(input("enter the first number:"))
n=int(input("enter the number of terms:"))
d=int(input("enter the common difference"))

nth_term= a+ (n-1)*d
Sn=n/2*(2*a + (n-1)*d)
print(f"the nth term is :{nth_term}")
print(f"the sum of the numbers: {Sn}")
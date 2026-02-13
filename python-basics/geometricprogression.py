#Name:Karen Mwaniki
#Date:13/02/2026
#Program to calculate geometric progression

#calculating the nth term

a = int(input("Enter the first term: "))  # first term
r = int(input("Enter the common ratio: "))  # common ratio
n = int(input("Enter the term number: "))  # term number

nth_term=a*(r**(n-1))

print(f"The {n}th term  is: {nth_term}")
#Name:Karen Mwaniki
#Date:17/02/2026
#program to perform arithmetic operations 

f_number=12
s_number=34
sum_numbers=f_number+s_number
difference=f_number-s_number
product=f_number*s_number
quotient=f_number/s_number

print("the sum of the numbers %d " %sum_numbers)
print("the quotient of the numbers %0.4f " %quotient)

#modulus- remainder
print(7%5)

#even and odd numbers
for x in range(0,21):
    if x%2==1:
        print(f"{x} is odd")
    elif x%2==0:
        print(f"{x} is even")
        
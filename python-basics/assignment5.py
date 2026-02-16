#Name:Karen Mwaniki
#Date:16/02/2026
#program to calculate income tax

salary=int(input("enter your gross salary:")) #capture the gross salary of the user

if salary<50000:
    tax=(2.5*salary)/100
    net_salary=salary-tax

    print(f"gross salary={salary}")
    print(f"net_salary={net_salary}")
    print(f"tax={tax}")

elif salary>=50000 and salary<100000:
    tax=(4.5*salary)/100
    net_salary=salary-tax

    print(f"gross salary={salary}")
    print(f"net_salary={net_salary}")
    print(f"tax={tax}")

elif salary>=100000:
    tax=(7.5*salary)/100
    net_salary=salary-tax

    print(f"gross salary={salary}")
    print(f"net_salary={net_salary}")
    print(f"tax={tax}")

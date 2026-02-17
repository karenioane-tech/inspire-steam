#Name:Karen Mwaniki
#Date:17/02/2026
#program to format the output in different styles

name="Karen Mwaniki" #name

weight=60 #weight in kgs

favourite_team="Manchester city"

height=1.65 #height in centimeters

 # 1formatting using printf (f"{}")

print(f"my name is {name} and i weigh {weight}kgs")

# 2 using f strings to format the output

msg= f"my name is {name} and i support {favourite_team}"
print(msg)

# 3 using curly brackets {} to format the output .format() method

print("my name is {0} and I am {1} centimeters tall".format(name,height))

# 4 using output specifiers to format the output %s-strings %f-floats %d-integers

print("i support %s" %favourite_team)

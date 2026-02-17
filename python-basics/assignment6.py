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




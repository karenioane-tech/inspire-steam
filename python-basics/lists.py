#Name:Karen Mwaniki
#Date:18/02/2026
#program to show lists in Python

#list of friends
friends=["Lorna","Felix","James","Saenyi","Molyne"]

print(friends)

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends.append("Ochieng")
print(friends)

new_friends=["Achieng","Mwangi","Precious","Ben"]

print(len(friends))

#new lists of students
students= friends+new_friends
print(students)

students.pop()
print(students)

students.insert(5,"Mwaniki")
print(students)
students.insert(7,"Renee")
print(students)

students.remove("Renee")
print(students)

new_students=students.copy()
print(new_students)
#Name:Karen Mwaniki
#Date:18/02/2026
#program to show dictionaries in Python

cars={"Model":"Mazda"
      ,"Make":"CX-5"
      ,"Year":2020
      ,"Color":"sundust bronze metallic"}
print(cars)

print(cars["Model"])
print(cars["Make"])
print(cars["Year"])
print(cars["Color"])

students=dict({"Saenyi":20,
              "Molyne":19,
              "Felix":21,
              "Lorna":22})

for key in students:
    print(key)

for val in students.values():
    print(val)


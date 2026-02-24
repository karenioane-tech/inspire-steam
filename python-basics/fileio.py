#Name:Karen Mwaniki
#Date:24/02/2026

#program to perform file operations

#create new file
new_file = open("student_data.txt", "r+")

#write new file
new_file.write("{Student Name:Karen Mwaniki, ID:25040308,email:karenmwaniki1@gmail.com}")
new_file.close()

#read to new file
new_file=open("student_data.txt", "r+")

data=new_file.read()
print(data)
new_file.close

#delete file
#use os module

import os
os.remove("remove.txt")

#delete folder
os.rmdir("folder")

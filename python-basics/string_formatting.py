#Name:Karen Mwaniki
#Date: 12/02/2026
#String Formatting

#get string length
sentence = "I am learning python"

string_length = len(sentence)

print(f"The length is:{string_length}")

#spliting a string
sentence_2= "Mathematics Physics"
split=sentence_2.split(" ")

print(f"The first subject is: {split[1]}")


#make everything uppercase
code= "kdg34kbrkdq"

capitalized=code.upper()

print(f"New code is: {capitalized}")

#make everything lowercase
code_2= "KDg34kbrkdq"

lowercase=code_2.lower()

print(f"New code is: {lowercase}")

#replace characters in a string

balance= "100Kes"
amount_added= "50Kes"

cleaned_balance= balance.replace("Kes","")

print(f"Cleaned balance is: {cleaned_balance}")

cleaned_amount_added= amount_added.replace("Kes","")

print(f"Cleaned amount added is: {cleaned_amount_added}")

#
new_balance= int(cleaned_balance) + int(cleaned_amount_added)

print(f"New balance is: {new_balance}")

new_balance_string= str(new_balance) 


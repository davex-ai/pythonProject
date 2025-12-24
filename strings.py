name = "DAVE"
print(f"My name is {name}")
print("My name is " + name)
name += " is my name"
print(name)

#Multi - lined String
print("""My
name is

dave""")

# String Methods
chair = "chAir"
print("String Methods")
print(chair.title()) #Capitalizes the first letter
print(chair.islower()) #Checks if it's all lowercase
print(chair.upper()) #Capitalizes the whole string
print(chair.isupper()) #Checks if it's all uppercase
print(chair.startswith("c"))# Checks what letter the string begins with
print(chair.endswith("r"))# Checks what letter the string ends with
print(chair.replace("chAir", "table"))# replace substring
print(chair.strip()) #to trim white spaces
print(chair.split("A"))#split a string on a character seperator
print(chair.join("e")) # to append new letters
print(chair.find("i")) # find position of a substring
print(chair.isalnum()) #checks for characters and digits
print(chair.isalpha()) #check if it contains a letter
print(chair.isdigit()) # check if it contains a digit
print(len(chair)) # return length of string
print("Ai" in  chair) # checks for substring

#String as Array
print("\n String as an array")
lang = "python"
print(lang[2])
print(lang[2:4])
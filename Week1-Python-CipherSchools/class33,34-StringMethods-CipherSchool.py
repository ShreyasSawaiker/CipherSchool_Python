name = "Sitansu Naik"

length = len(name) #lenght fucntion
print(length)

print(name.lower())# converts string to lower case
print(name.upper())# converts string to uper case

print(name.title())# first letter upercase

print(name.count("s")) #counts the number of recurrences of partcular letter


#*********************************************************************************************
#Excersise -> String

name,char =input("comma sep name: ").split(",")
print(f"length of your name:{len(name)}")
print(f"character count:{name.lower().count(char)}")

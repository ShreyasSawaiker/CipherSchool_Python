#IF Elif Statements

age = int(input("Enter Your Age:"))
if(age == 0):
    print("You Can't Watch")
elif(age >= 10 and age <= 20):
    print("Ticket Price Is 100")
elif(age >= 21 and age <= 50):
    print("Ticket Price is 250")
else:
    print("Ticket Price is 200")


# IN Keyword Python
name2 = "Shrey"
if('a' in name2):
    print("a is in name")
else:
    print("letter is not there")

# Check is string is empty or not
name3 = "abc"
if name3:
    print("Something")
else:
    print("Nothing")
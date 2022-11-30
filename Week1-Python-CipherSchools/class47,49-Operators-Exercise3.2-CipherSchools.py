# AND Statement is used to check more than one conditions 
# It return true if both all condititons are true

name='abc'
age =18
if name=='abc' and age==18:
    print("condition true")
else:
    print("false")

# OR Statement return true if any one condititons is true
name2='abcd'
age =18
if name2=='abc' or age==18:
    print("condition true")
else:
    print("false")

#****************************************************************
#Exercise 3
name=input("enter your name: ")
age=int(input("enter your age:"))
if (name[0]=='a' or name[0]=='A')and age > 10:
    print("you can watch")
else:
    print("you can naot watch")
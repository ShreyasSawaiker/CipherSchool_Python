# class 55 Exercise

# n=int(input("enter number:"))
# total=0
# i=1
# while i<=n:
#     total+=i
#     i+=1
# print(total)

# # class 57 exercise

# n=input("enter a number:")
# total=0
# # int(number[i])
# i=0
# while i<len(n):
#     total+=int(n[i])
#     i+=1
# print(total)

# class 59 exercise

name = input("enter your name:")
temp_var=""
i=0
while i<len(name):
    if name[i] not in temp_var:
        temp_var +=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1
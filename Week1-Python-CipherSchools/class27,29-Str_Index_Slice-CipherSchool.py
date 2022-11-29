language = "Python"

print(language[2])
print(language[4])
# print(language[5]) # error because string indexing happens within the range

print(language[-1]) # return the last character
print(language[-2]) # negative index returns from last


#***********************************************************
# String Slicing means selcting the sub string
# Syntax = [start:end]
print(language[2:4])
print(language[3:5])

print("Shrey"[1:4])
print("YeahMan"[0:5:2])
print("YeahMan"[5::-1])
print("Man"[::-1])


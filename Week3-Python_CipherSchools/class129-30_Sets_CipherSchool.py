# unoerderd collection of unique items

s = {1,2,3,3}
print(s)
#indexing doesnt work with sets

l = [1,1,1,2,2,2,3,3,3]
s2 = set(l)
print(s2)

#set methods
s.add(4)
print(s)
s.remove(3)
print(s)

s.discard(7) #wont get error if element is not present
# s.clear method clears the set

s3 = {'a','b','c'}

for i in s3:
    print(i)

# set maths
s4 = {1,2,3,4,5}
s5 = {5,6,7,3}

unionset = s4 | s5
print(unionset)

interset = s4 & s5
print(interset)
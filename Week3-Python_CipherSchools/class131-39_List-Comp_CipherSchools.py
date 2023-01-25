#general method
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

#using list comprehension
squares2 = [i**2 for i in range(1,11)]
print(squares2)
neg_list = [-i for i in range(1,11)]
print(neg_list)

names = ["Shrey","baymax","Robot"]
newlist = [i[0] for i in names]
print(newlist)

#Ecercise 1
def reversestrings(l):
    return [i[::-1] for i in l]

print(reversestrings(names))

# if statements in list comprehension
nums = list(range(1,11))
even = [i for i in nums if i%2 == 0]
odd = [i for i in range(1,11) if i%2 != 0]
print(even)
print(odd)


#Exercise 2
def num(l):
    return [str(i) for i in l if(type(i) == int or type(i) == float)]

mlist = ["yep",1,5,2,5.2,3.5,[1,2,3]]
print(num(mlist))


#if else in list comprehension
newnums = [i*2 if i%2 == 0 else -i for i in nums]
print(newnums)


#nested list comprehension
neslist = [[1,2,3],[4,5,6],[7,8,9]]
neslist2 = [[i for i in range(1,4)] for j in range(3)]
print(neslist2)
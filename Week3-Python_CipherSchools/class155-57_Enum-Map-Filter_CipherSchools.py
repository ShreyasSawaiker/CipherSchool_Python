# enum function

names = ['shrey','baymax','root']
for pos,name in enumerate(names):
    print(f"{pos} ---> {name}")


def findpos(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
        return -1

print(findpos(names,'shrey'))

# Map function in python
numbers = [1,2,3,4,5]

def sq(a):
    return a**2

sqaures = list(map(lambda a:a**2,numbers))
print(sqaures)

# using list compre
squares2 = [i**2 for i in numbers]
print(squares2)

# map funcs are iterable


# filter fcuntion
# filter function is iterable
num2 = [1,2,3,4,5,6,7,8,9,10]
is_even = lambda a: a%2==0
even = list(filter(is_even,num2))
print(even)
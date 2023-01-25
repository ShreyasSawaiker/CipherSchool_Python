# *args take multiple inputas tuple
def alltotal(*args):
    total = 0
    for num in args:
        total += num
    return total

print(alltotal(1,2,3,4))
nums = [5,5]
print(alltotal(*nums))

#exercise 1
def power(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return "empty arggs"

print(power(2,*nums))
print(power(2,*[1,2,3]))    

# **kwargs

def func(**kwargs):
    print(kwargs)

func(first_name = "Shrey" , last_name = "Robot")

def func2(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

dict = {'age' : 12, 'name' : "Root"}
func2(**dict)

# PADK Order func
def func3(name,*args,lastname = "unknown", **kwargs):
    print(name)
    print(args)
    print(lastname)
    print(kwargs)

func3("SHrey",1,2,3,a = 1, b = 2)

#Exercise 2
def capfunc(l,**kwargs):
    if kwargs.get('reverse_string') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names = ['harshit','mohit']
print(capfunc(names,reverse_string = True))
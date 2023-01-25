# create sqdict{1:1, 2:4, 3:9}
sqdict = {num:num**2 for num in range(1,11)}
print(sqdict)

sqdict2 = {f"square of {num} is":num**2 for num in range(1,11)}
#print(sqdict2)
for k,v in sqdict2.items():
    print(f"{k} : {v}")

# word counter using list compre
string = "Baymax"
word_count = {char:string.count(char) for char in string}
print(word_count)

# dictionary comprehension with if else
odd_even = {i: ('even' if i%2 == 0 else 'odd') for i in range(1,5)}
print(odd_even)

#sets comprehension
s = {k**2 for k in range(1,11)}
print(s)
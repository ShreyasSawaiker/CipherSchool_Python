user = ['user1','user2','user3']
name = ['shrey','bro','niki']

print(list(zip(user,name)))

l= [(1,2),(3,4),(5,6)]
print(*l)
l1, l2 = list(zip(*l))
print(l1)
print(l2)

numl1 = [1,2,3]
numl2 = [2,5,6]
newl = []

for pair in zip(numl1,numl2):
    newl.append(max(pair))

print(newl)
# List
myfriends =['jingfangning','luxin']
print(myfriends)
print(len(myfriends))
print(myfriends[-1])

myfriends.insert(1,'maheng')
print(myfriends)

myfriends.append('luojun')
print(myfriends)
myfriends.pop()
print(myfriends)


L=list(range(100))
print(L)
print(L[:10])
print(L[::4])
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]



i=0

while i<len(L):
    j = 0
    while j<len(L[i]):
        print(L[i][j])
        j=j+1
    i=i+1


# Tuple
classmates = ('Michael', 'Bob', 'Tracy')


# Dict
fractionalTable={'fangzongzhou':80,'guoranran':90}
print(fractionalTable['guoranran'])
fractionalTable['guoranran']=95
print(fractionalTable['guoranran'])
print('fangzongzhou' in fractionalTable)
print(fractionalTable.get('guoranran'))
print(fractionalTable)
fractionalTable.pop('fangzongzhou')
print(fractionalTable)

# Set
myset=set([1,1,2,3,44,44])
print(myset)
myset.add(44)
print(myset)
myset.remove(44)
print(myset)

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

# ageStr=input('please input your age')
# age=int(ageStr)
# if age>18:
#     print('adult')
# else:
#     print('tennger')


file = open('hello.py','r')
print(file.read())
file.close()


try:
    f=open('hello.py','r')
    print(f.read())
finally:
    if f:
        f.close()

with open('hello.py','r') as f :
    print(f.read())

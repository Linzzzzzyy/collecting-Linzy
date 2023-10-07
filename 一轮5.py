user={1:"name1",2:"name2",3:"name3"}

keys=[]

for key in user:
    a=key
    if a%2==0:
        keys.append(a)

user.pop(a-1)
print(user)

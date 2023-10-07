x=int(input("请输入"))
y=int(input("请输入"))
z=int(input("请输入"))
last=None
if x>=y:
    m=x
    mid=y
else:
   m=y
   mid=x
if m<=z:
   last=mid
   mid=m
   m=z

elif mid>=z:
   last=z
print(m,mid,last)

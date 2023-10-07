def __init__(item):
    item={"商品序号":"0","商品名":"Unknow","单价":"0.0","总数量":"0","剩余数量":"0"}
    return item
def display(item):
    print("商品序号是：",item["商品序号"])
    print("商品名是：",item["商品名"])
    print("单价是：",item["单价"])
    print("总数量是：",item["总数量"])
    print("剩余数量是：",item["总数量"]) 

def income(item):
    a=item["总数量"]
    b=item["剩余数量"]
    c=item["单价"]
    income=(a-b)*c
    return income
def setdata(number,name,price,total,remain):
    item["商品序号"]=number
    item["商品名"]=name
    item["单价"]=price
    item["总数量"]=total
    item["剩余数量"]=remain
    return item


item={"商品序号":"1234","商品名":"辣条","单价":5.5,"总数量":15,"剩余数量":7}




__init__(item)
display(item)
number=input("请输入想要更改的数值：")
name=input("请输入想要更改的数值：")
price=input("请输入想要更改的数值：")
total=input("请输入想要更改的数值：")
remain=input("请输入想要更改的数值：")

setdata(number,name,price,total,remain)
print(item)

a=income(item)
print("已售出商品的价值：",a)

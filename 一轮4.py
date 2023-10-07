sum_list=input("请输入").split()

i=0
number_list=[]
while(i<len(sum_list)):
    if sum_list[i].isdigit()==True:
       number_list.append(sum_list[i]) 
    i=i+1
print(sorted(number_list))

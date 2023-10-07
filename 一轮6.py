def account(list_):
    number={}
    
    i=len(list_)
    while(i>0):
        a=1
        while(j>0):
            j=i+1
            if list_[i]==list_[j]:
               a=a+1
               del list_[j]
        number.setdefault(i,a)
    return number

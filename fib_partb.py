lst=[1,3]
n=int(input("enter the number:"))
i=1
while(i<=n):
    next_element=sum(lst[i-1:i+1])
    lst.append(next_element)
    i+=1
print((lst))


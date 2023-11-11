a=[1,2,3,4,5,6,7,8,9]
b=[]
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
c=[]
i=0
while(i<len(b)):
    c.append(b[i])
    i+=2
print(c)
print(c[1])


print(b)

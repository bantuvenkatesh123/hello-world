a=[2,1,4,3]
for x in range(0,len(a)):
    for y in range(0,len(a)-1):
        if(a[y]>a[y+1]):
            b=a[y]
            a[y]=a[y+1]
            a[y+1]=b
print(a)

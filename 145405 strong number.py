a=int(input("enter 145 or 405"))
x=a
s=0
while(a>0):
    b=int(a%10)
    f=1
    if(b==0):
        f=1
    else:
        for i in range(1,b+1):
            f=f*i
    s=s+f
    a=int(a/10)
print(s)

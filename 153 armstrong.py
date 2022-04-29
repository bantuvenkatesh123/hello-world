a=int(input())
x=a
s=0
while(a>0):
    b=int(a%10)
    s=s+(b*b*b)
    a=int(a/10)
print(s)

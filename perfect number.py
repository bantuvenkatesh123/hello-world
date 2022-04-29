a=int(input("enter 6 or 28 or 496 or 8128"))
b=0
for i in range(1,a):
    if(a%i==0):
        b=b+i
if(a==b):
    print("perfect number")
else:
    print("not a perfect number")

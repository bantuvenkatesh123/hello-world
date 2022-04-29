a=input()
b=' '
for i in range(0,len(a)):
    b=a[i]+b
    print(b)
if(a==b):
    print("palindrome")
else:
    print("not a palindrome")

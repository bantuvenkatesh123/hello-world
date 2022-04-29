#def sum(a,b):
#    return a+b
#if __name__=='__main__':
#    a = int(input('enter a value'))
#   b = int(input('enter b value'))
#    print(sum(a,b))
#def factorial(x):
#    if x==1:
#        return 1
#    else:
#        return x*factorial(x-1)
#if __name__=='__main__':
#    x=int(input('emter x vlue'))
#    print(factorial(x))
#if __name__=='__main__':
 #   a=lambda x: x*x
 #   x=int(input('enter argument x value'))
#    print(a(x))
#if __name__=='__main__':
 #   a=lambda x,y: x*y
 #   x=int(input('enter argument x value'))
 #   y = int(input('enter argument y value'))
#    print(a(x,y))
#if __name__=='__main__':
 #   a=lambda x: print('even') if x%2==0 else print('odd')
  #  x=int(input('enter argument x value'))
   # a(x)
if __name__=='__main__':
    factorial=lambda x: 1 if x==1 else x*factorial(x-1)
    x = int(input('enter argument x value'))
    print(factorial(x))

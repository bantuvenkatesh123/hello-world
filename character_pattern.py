number=int(input("a for 65"))
rows=int(input("rows number"))
for i in range(0,rows):
    number=65
    for j in range(0,i+1):
        character=chr(number)
        print(character,end='')
        number=number+1
    print()

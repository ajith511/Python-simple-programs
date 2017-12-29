print('Welcome to calculator')
print('choose which operation to be initiated\n 1.Multiplication \t 2. Division \t 3. Addition \t  4. Substraction \t 5. Modular Division \t 6. Power ')
c = int(input('enter operation number: '))


a = int(input('enter a number to be calculated'))
b= int(input('enter number to be calculated'))

if c == 1:
    print(a*b)
elif c == 2:
    print(a//b)
elif c == 3:
    print(a+b)
elif c == 4:
    print(a-b)
elif c == 5:
    print(a%b)
elif c == 6:
    print(a**b)
else :
    print ('invalid operation')

print('Enter integer numbers, enter [.] to end sequence')
odd = 0
even = 0
first = True
a = raw_input('->')
while first or a != '.':
    if a !='' and (a.isdigit() or (a[0] == "-" and a[1:].isdigit())):
        first = False
        a = int(a)
        if a % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    else:
        print('Not is integer')
    a = raw_input('->')
print('odd count = ' + str(odd))
print('even count = ' + str(even))
quit()

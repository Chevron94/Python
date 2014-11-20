import math
def remove_extra_characters_after_the_decimal_point(n):
    def inner_decorator(function_to_wrap):
        def inner_function(arg):
            res = function_to_wrap(arg)
            if res != None:
                print(('{0:.'+str(n)+'f}').format(res))
            return res
        return inner_function
    return inner_decorator

@remove_extra_characters_after_the_decimal_point(4)
def SQRT(arg):
    return math.pow(math.fabs(arg),0.5)

print('Enter integer number')
a = raw_input('->')
Correct = False
while Correct == False:
    if a !='' and (a.isdigit() or (a[0] == "-" and a[1:].isdigit())):
        a = int(a)
        Correct = True
    else:
        print('Not is integer')
        a = raw_input('->')
SQRT(a)
exit()

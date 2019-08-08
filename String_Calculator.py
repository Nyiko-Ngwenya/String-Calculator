import re
def addition(a,b):
    sum = 0
    if a == '' or b == '':
        if a == '' and b == '':
            a = 0
            b = 0 
        elif b == '':
            b == 0
        else:
            a = 0  
    print(int(b))          
    sum = int(a)+int(b)
    return sum

def addition2(*args):
    sum = 0
    for number in args:
        if number == '':
            number = 0
        sum += int(number)
    return sum

def addition_proper(a):
    arr = a.split(',')
    print(arr)
    sum = 0
    for number in arr:
        if number == '':
            number = 0
        if str.contains('n') in number:
            print('True')
        #sum += int(number)
    return sum
print(addition_proper('10\n5,5'))
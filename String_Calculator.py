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

print(addition('',''))

def addition2(*args):
    sum = 0
    for number in args:
        if number == '':
            number = 0
        sum += int(number)
    return sum



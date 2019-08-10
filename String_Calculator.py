import regex as re
import numpy as np

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
    #arr = a.split(',')
    pattern = "\d+"
    #result = re.findall(pattern, string) 
    arrayy = re.findall(pattern, a) 
    print(arrayy)
    sum = 0
    for number in arrayy:
        #print(type(number))
        if number == '':
            number = 0
            #x = re.sub("\n", number)
        sum += int(number)
        print(sum)
    return sum



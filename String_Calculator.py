import re
import numpy as np

# def addition_proper(a):
#     #arr = a.split(',')
#     pattern = "\d+"
#     #result = re.findall(pattern, string) 
#     arrayy = re.findall(pattern, a) 
#     print(arrayy)
#     sum = 0
#     for number in arrayy:
#         #print(type(number))
#         if number == '':
#             number = 0
#             #x = re.sub("\n", number)
#         sum += int(number)
#         print(sum)
#     return sum

def Add(strings):
    count = 0
    if strings == '':
        return 0
    elif ',' in strings:
        for number in strings.split(', | \n'):
            count += int(number)
        return count
    else:
        return int(strings)


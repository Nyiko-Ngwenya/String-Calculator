import re
import numpy as np

def Add(strings):
    count = 0
    pattern = r'-?\d+'
    arrayy = re.findall(pattern, strings)
    arrayNeg = []
    if strings == '':
        return 0
    if arrayy:
        for number in arrayy:
            if int(number) < 0:
                raise Exception(f'this {number} is a negative')
            else:    
                count += int(number)
        return count    
    else:
        return 0

#print(Add('//;\n18;2') )
# pattern = '-?\d'
# stringz = '1,2'
# stringz = '-1,2'
# stringz = '1\n2,3'

# match = re.search(pattern,stringz)
# arrayy = re.findall(pattern, stringz) 
# print(arrayy)
# sum = 0

# for number in arrayy:
#     print(number)
    #print(type(number))
    #sum += int(number)
        #x = re.sub("\n", number)
#     sum += int(number)
    
# print(sum)

# print(match)

def Add_version_2(strings):
    count = 0
    pattern = r'-?\d+'
    arrayy = re.findall(pattern, strings)
    if strings == '':
        return 0
    if arrayy:
        for number in arrayy:
            count += int(number)
        return count    
    else:
        return 0   


import re
import numpy as np

def Add(strings):
    count = 0
    if strings == '':
        return 0
    elif ',' in strings:
        pattern = r'\d+'
        arrayy = re.findall(pattern, strings) 
        for number in arrayy:
            #print(number)
            count += int(number)
        #return arrayy
        return count
    elif ';' in strings:
        pattern = r'\d+'
        arrayy = re.findall(pattern, strings) 
        for number in arrayy:
            #print(number)
            count += int(number)
        #return arrayy
        return count
    elif '-' in strings:
        pattern = r'-?\d+'
        arrayy = re.findall(pattern, strings) 
        for number in arrayy:
            #print(number)
            count += int(number)
        #return arrayy
        return count
    else:
        return int(strings)

print(Add('//;\n18;2') )
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

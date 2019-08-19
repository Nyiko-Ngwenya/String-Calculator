import re
import numpy as np

def Add(strings):
    if strings == '':
        return 0
    count = 0
    pattern = r'-?\d+'
    arrayy = re.findall(pattern, strings)
    arrayNeg = [negative for negative in arrayy if '-' in negative]
    if arrayNeg:
        if len(arrayNeg) > 1:
            raise Exception(f'these are {arrayNeg} negative')
        else:
            raise Exception(f'this {arrayNeg} is a negative ,negatives not allowed')
    if arrayy:
        for number in arrayy:
            if int(number) < 1000:
                count += int(number)    
        return count    
    else:
        return 0


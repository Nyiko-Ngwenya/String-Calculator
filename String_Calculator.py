import re

def Add(strings):
    #checking if string empty
    if strings == '':
        return 0
    #creating count to keep track of number    
    count = 0
    #this will be the pattern that finds all numbers positive and negatives
    pattern = r'-?\d+'
    collectedNumbers = re.findall(pattern, strings)
    #this will collect all the negative numbers
    arrayNeg = [negative for negative in collectedNumbers if '-' in negative]
    if arrayNeg:
        if len(arrayNeg) > 1:
            raise Exception(f'these are {arrayNeg} negative')
        else:
            raise Exception(f'this {arrayNeg[0]} is a negative ,negatives not allowed')
    if collectedNumbers:
        for number in collectedNumbers:
            if int(number) < 1000:
                count += int(number)    
        return count    
    else:
        return 0


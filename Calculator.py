import matplotlib.pyplot as plt
import re


#print(mo.group(3))
x = 3



#finds the coefficient of the term

"""make a regex manually"""
def finder(x, input):
    regex_count = 0 # number of items in regex
    regex = "(.*)"
    regex_count += input.count("+")
    regex_count += input.count("-")
    for i  in range(regex_count):
            regex += "[+-](.*)"
    # seperates the terms to be added using regex
    QuadraticRegex = re.compile(rf'{regex}')
    print(regex)
    mo = QuadraticRegex.search(input)

    result = 0
    
    for item in mo.groups():
        
        #manually makes the regex
        if ("x" in item) == False:
            result += int(item)
            continue
        power = 1
        
        #int the index of the power
        termRegex = re.compile(r"x\^(\d+)")
        index = termRegex.search(item)
        
        # finds the power
        if index != None:
            power = int(index.group(1))
        
        y = pow(x,power)
            
        #finds the coeeficient
        coefficientRegex = re.compile(r'(\d+)(?=x)')
        coefficient = coefficientRegex.search(item)
        #multiplies by the co
        y= int(coefficient.group(0)) * y
        result += y
    return result
x = [1,2,3,4,5,6,7,8]
input = "2x+1"
y_list = [finder(x, input) for x  in x]
print(y_list)
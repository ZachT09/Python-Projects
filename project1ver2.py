#PEMDAS
#Parenthesis, Exponent, Multiplication, Division, Addition, Subtraction
#Reverse order from top to bottom for functions
def clearParenthesis(equationString):
    while " ".join(equationString).find("(") != -1:
        i = 0
        if equationString[i] == "(":
            equationString[i] = [""]
            continue
        i += 1
        
    while " ".join(equationString).find(")") != -1:   
        i = 0
        if equationString[i] == ")":
            equationString[i] = [""]
            continue
        i += 1
    return equationString

def checkIfDone(equationString):
    if equationString.find("-") or equationString.find("+") or equationString.find("x") or equationString.find("*") or equationString.find("/") or equationString.find("^") or equationString.find("("):
        return False
    else:
        return True

def findSubtraction(equationString):    
    for i, value in enumerate(equationString):
        if value == "-":
            num1 = int(equationString[i - 1])
            num2 = int(equationString[i + 1])
            equationString[i-1:i+2] = [num1 - num2]
    return equationString

def findAddition(equationString):
    for i, value in enumerate(equationString):
        if value == "+":
            num1 = int(equationString[i - 1])
            num2 = int(equationString[i + 1])
            equationString[i-1:i+2] = [num1 + num2]
    return equationString

def findDivision(equationString):
    for i, value in enumerate(equationString):
        if value == "/":
            num1 = int(equationString[i - 1])
            num2 = int(equationString[i + 1])
            equationString[i-1:i+2] = [num1 / num2]
    return equationString

#STILL IN PROGRESS
#TODO:
# Make function grab first number (num to the left of the multiplication equation) and second number (opposite)
# Return the string with said number replacing the space the equation was in before
def findMultiplication(equationString):
    for i, value in enumerate(equationString):
        if value == "*":
            num1 = int(equationString[i - 1])
            num2 = int(equationString[i + 1])
            equationString[i-1:i+2] = [num1 * num2]
    return equationString


def findExponent(equationString):
    if type(equationString) is not list:
        newEQ = equationString.split()
    else:
        newEQ = equationString
    for i, value in enumerate(newEQ):
        if value == "^":
            num1 = int(newEQ[i - 1])
            num2 = int(newEQ[i + 1])
            newEQ[i-1:i+2] = [num1 ** num2]
    return newEQ

def findParenthesis(equationString, start, end):
    if type(equationString) is list:
        equationString = " ".join(equationString)
    if equationString.find("(") >= 0:
        target_start = equationString.find("(")
        open_parenthesis = 1
        i = target_start
        while i < len(equationString):
            if equationString[i] == ')' and open_parenthesis == 1:
                break
            if equationString[i] == '(':
                open_parenthesis += 1
            i += 1
        
        if open_parenthesis == 1:
            target_end = equationString.find(")", target_start)
            equationString = findParenthesis(equationString, target_start + 1, target_end - 1)
            equationString = findExponent(equationString)
            equationString = findMultiplication(equationString)
            equationString = findDivision(equationString)
            equationString = findAddition(equationString)
            equationString = findSubtraction(equationString)
            return equationString
        else:
            #open_parenthesis will count the amount of other sets of parenthesis within the equation
            #to get to the right set of parenthesis it needs to pass 
            for i in range(open_parenthesis):
                target_start = equationString.find("(", target_start)
                target_end = equationString.find(")", target_start)
                equationString = findExponent(equationString)
                equationString = findMultiplication(equationString)
                equationString = findDivision(equationString)
                equationString = findAddition(equationString)
                equationString = findSubtraction(equationString)
        target_start = equationString.find("(")
        target_end = equationString.find(")", target_start)
        equationString[target_start:target_end + 1] = [equationString[target_start + 1]]
        return equationString
 
def convertVars(equationString, num):
    while equationString.find("x") != -1:
        y = equationString.find('x')
        if y != -1:
            start_of_coefficient = equationString.find(" ", y)
            if start_of_coefficient >= y:
                start_of_coefficient = 0
            if start_of_coefficient == -1:
                newString = equationString[0:y]
                equationString = equationString.replace(equationString[0 : y], str(int(newString) * num))
                return equationString
            elif start_of_coefficient == int(y) - 1:
                equationString = equationString.replace(equationString[y], str(num))
                return equationString
            else:
                newString = equationString[start_of_coefficient : y]
                print(newString)
                equationString.replace(equationString[start_of_coefficient : y], str(int(newString) * num)) 
                return equationString       

def returnEquationValue(num, equationString):
    equationString = convertVars(equationString, num)
    equationString = findParenthesis(equationString, None, None)
    #equationString = clearParenthesis(equationString)
    print("passing")
    equationString = findExponent(equationString)
    equationString = findMultiplication(equationString)
    equationString = findDivision(equationString)
    equationString = findAddition(equationString)
    equationString = findSubtraction(equationString)
    return equationString

def drawGraph(size, eq):
    for x in range(int(size)):
        print(f"x = {x} -> ", returnEquationValue(x, eq))

print(
"""
Formatting rules:
    -Range will start at 0 like a normal graph, first value will always be 0 incrementing by 1 each value after
    -For multiplication use "*"
    -For Division use /
    -Put spaces (one space) between numbers and methods (3x - 2)
"""
)


drawGraph(input("What is the range you would like "), input("What is the equation "))

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

# Combined Left-to-Right for Addition and Subtraction
def findAddSub(equationString):
    if type(equationString) is not list:
        newEQ = equationString.split()
    else:
        newEQ = equationString
        
    while "+" in newEQ or "-" in newEQ:
        # Find index of the first appearance of + or - from left to right
        try:
            i_add = newEQ.index("+")
        except ValueError:
            i_add = float('inf')
            
        try:
            i_sub = newEQ.index("-")
        except ValueError:
            i_sub = float('inf')
            
        if i_add < i_sub:
            i = i_add
            num1 = float(newEQ[i - 1])
            num2 = float(newEQ[i + 1])
            newEQ[i-1:i+2] = [str(num1 + num2)]
        else:
            i = i_sub
            num1 = float(newEQ[i - 1])
            num2 = float(newEQ[i + 1])
            newEQ[i-1:i+2] = [str(num1 - num2)]
    return newEQ

# Combined Left-to-Right for Multiplication and Division
def findMulDiv(equationString):
    if type(equationString) is not list:
        newEQ = equationString.split()
    else:
        newEQ = equationString
        
    while "*" in newEQ or "/" in newEQ:
        try:
            i_mul = newEQ.index("*")
        except ValueError:
            i_mul = float('inf')
            
        try:
            i_div = newEQ.index("/")
        except ValueError:
            i_div = float('inf')
            
        if i_mul < i_div:
            i = i_mul
            num1 = float(newEQ[i - 1])
            num2 = float(newEQ[i + 1])
            newEQ[i-1:i+2] = [str(num1 * num2)]
        else:
            i = i_div
            num1 = float(newEQ[i - 1])
            num2 = float(newEQ[i + 1])
            newEQ[i-1:i+2] = [str(num1 / num2)]
    return newEQ

def findExponent(equationString):
    if type(equationString) is not list:
        newEQ = equationString.split()
    else:
        newEQ = equationString
    while "^" in newEQ:
        i = newEQ.index("^")
        num1 = float(newEQ[i - 1])
        num2 = float(newEQ[i + 1])
        newEQ[i-1:i+2] = [str(num1 ** num2)]
    return newEQ

def findParenthesis(equationString, start, end):
    if type(equationString) is list:
        equationString = " ".join(equationString)
    if equationString.find("(") == -1:
        return equationString
        
    target_start = equationString.find("(")
    open_parenthesis = 1
    i = target_start + 1
    while i < len(equationString):
        if equationString[i] == ')' and open_parenthesis == 1:
            target_end = i
            break
        if equationString[i] == '(':
            open_parenthesis += 1
        elif equationString[i] == ')':
            open_parenthesis -= 1
        i += 1
    
    sub_eq = equationString[target_start + 1: target_end]
    sub_eq = findExponent(sub_eq)
    sub_eq = findMulDiv(sub_eq)
    sub_eq = findAddSub(sub_eq)
    
    if type(sub_eq) is list:
        sub_eq = " ".join(sub_eq)
        
    equationString = equationString[:target_start] + sub_eq + equationString[target_end + 1:]
    
    if equationString.find("(") != -1:
        equationString = findParenthesis(equationString, None, None)
        
    return equationString
 
def convertVars(equationString, num):
    if type(equationString) is list:
        equationString = " ".join(equationString)
        
    for digit in range(10):
        equationString = equationString.replace(str(digit) + "x", str(digit) + " * x")
        
    equationString = equationString.replace("x", str(num))
    return equationString

def returnEquationValue(num, equationString):
    equationString = convertVars(equationString, num)
    equationString = findParenthesis(equationString, None, None)
    equationString = findExponent(equationString)
    equationString = findMulDiv(equationString)
    equationString = findAddSub(equationString)
    
    if type(equationString) is list and len(equationString) == 1:
        return float(equationString[0])
    elif type(equationString) is list:
        equationString = " ".join(equationString)
        
    # Convert final string result to float to clean up decimals if desired
    try:
        return float(equationString)
    except ValueError:
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
    -Coefficients like 3x work automatically!
"""
)

drawGraph(input("What is the range you would like "), input("What is the equation "))
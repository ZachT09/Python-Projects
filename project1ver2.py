#PEMDAS
#Parenthesis, Exponent, Multiplication, Division, Addition, Subtraction
#Reverse order from top to bottom for functions
def checkIfDone(equationString):
    if equationString.find("-") or equationString.find("+") or equationString.find("x") or equationString.find("*") or equationString.find("/") or equationString.find("^") or equationString.find("("):
        return False
    else:
        return True

def findSubtraction(equationString, start, end, num):    
    pass

def findAddition(equationString, start, end, num):
    pass

def findDivision(equationString, start, end, num):
    pass

#STILL IN PROGRESS
#TODO:
# Make function grab first number (num to the left of the multiplication equation) and second number (opposite)
# Return the string with said number replacing the space the equation was in before
def findMultiplication(equationString, start, end, num):
    if start is not None:
        while equationString.find("*", start, end) != -1:
            y = equationString.find('*')
            if y != -1:
                start_of_coefficient = equationString.rfind(" ", start)
                start_of_coefficient = equationString.rfind(" ", start_of_coefficient)
                if start_of_coefficient == -1:
                    newString = equationString[0:y]
                    num1 = int(newString)
                    #equationString = equationString.replace(equationString[0 : y], str(int(newString) * num))
                else:
                    newString = equationString[start_of_coefficient : y]
                    num1 = int(newString)
                    #equationString.replace(equationString[start_of_coefficient : y], str(int(newString) * num))

                start_of_coefficient2 = equationString.find(" ", start)
                end_of_coefficient2 = equationString.rfind(" ", start_of_coefficient2)
                if start_of_coefficient == -1:
                    newString = equationString[y : len(equationString)]
                    num2 = int(newString)
                   
                else:
                    newString = equationString[y : end_of_coefficient2]
                    num2 = int(newString)
                equationString = equationString.replace(int(num1) * int(num2), start_of_coefficient, end_of_coefficient2)
                return equationString
                    
    else:
        while equationString.find("*", start, end) != -1:
            y = equationString.find('*', start, end)
            if y != -1:
                start_of_coefficient = equationString.rfind(" ", end, start)
                if start_of_coefficient == -1:
                    newString = equationString[0:y]
                    equationString = equationString.replace(equationString[0 : y], str(int(newString) * num))
                else:
                    newString = equationString[start_of_coefficient : y]
                    equationString = equationString.replace(equationString[start_of_coefficient : y], str(int(newString) * num))



def findExponent(equationString, start, end):
    pass

def findParenthesis(equationString, start, end):
    if equationString.find("(") >= 0:
        target_start = equationString.find("(")
        open_parenthesis = 1
        i = target_start
        while i < len(equationString - 1):
            i += 1
            if equationString[i] == ')' and open_parenthesis == 1:
                break
            if equationString[i] == '(':
                open_parenthesis += 1
        if open_parenthesis == 1:
            target_end = equationString.find(")", target_start)
            findParenthesis(equationString, target_start + 1, target_end - 1)
            findExponent(equationString, target_start + 1, target_end - 1)
            findMultiplication(equationString, target_start + 1, target_end - 1)
            findDivision(equationString, target_start + 1, target_end - 1)
            findAddition(equationString, target_start + 1, target_end - 1)
            findSubtraction(equationString, target_start + 1, target_end - 1)
        else:
            #open_parenthesis will count the amount of other sets of parenthesis within the equation
            #to get to the right set of parenthesis it needs to pass 
            for i in range(open_parenthesis):
                target_start = equationString.find("(", target_start)
                target_end = equationString.find(")", target_start)
                findExponent(equationString, target_start + 1, target_end - 1)
                findMultiplication(equationString, target_start + 1, target_end - 1)
                findDivision(equationString, target_start + 1, target_end - 1)
                findAddition(equationString, target_start + 1, target_end - 1)
                findSubtraction(equationString, target_start + 1, target_end - 1)
 
def convertVars(equationString, num):
    while equationString.find("x") != -1:
        y = equationString.find('x')
        if y != -1:
            start_of_coefficient = equationString.rfind(" ", y)
            if start_of_coefficient == -1:
                newString = equationString[0:y]
                equationString = equationString.replace(equationString[0 : y], str(int(newString) * num))
            elif start_of_coefficient == int(y) - 1:
                equationString = equationString.replace(equationString[y], str(num))
            else:
                newString = equationString[start_of_coefficient : y]
                equationString.replace(equationString[start_of_coefficient : y], str(int(newString) * num))        

def returnEquationValue(num, equationString):
    equationString = convertVars(equationString, num)
    equationString = findParenthesis(equationString)
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

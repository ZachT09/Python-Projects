
def returnEquationValue(num, equationString):
    #for each character in the equation check if there is a variable (x)
    for x in equationString:
        if x == 'x':
            #if there is an x in the equation find the index of it, then grab each character connected to it by inversely iterating and appending this into a new string
            y = equationString.find(x)
            start_of_coefficient = equationString.find(" ", y, -1)
            if start_of_coefficient == -1:
                newString = equationString[0:y]
            else:
                newString = equationString[start_of_coefficient : y]
            return int(newString) * num

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

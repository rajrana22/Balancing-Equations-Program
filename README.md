# Balancing-Equations-Program
A program that can take a chemical equation as input and output the same equation, but balanced.

# Code
import re
equation = "2H_2 + 0_2 = 2H_20"

elements = re.findall(r'([A-Z][a-z]*|[0-9])', equation, re.M)
for e in elements:
    print(e)

def right_side_elements(elements):
    for e in elements:
        if equation.index("e") > equation.index("="):
            return(e)

def left_side_elements(elements):
    for e in elements:
        if equation.index("e") < equation.index("="):
            return(e)

if left_side_elements(elements) == right_side_elements(elements):
    return equation
else:
    balanced = set left_side_elements(elements) == right_side_elements(elements)

final = normal + balanced

print "This is the balanced equation:" + final

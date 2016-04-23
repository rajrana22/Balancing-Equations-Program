# Balancing-Equations-Program
A program that can take a chemical equation as input and output the same equation, but balanced.

import re
equation = "2H_2 + 0_2 = 2H_20"
#how do I differenciate subscripts and coefficients?

elements = re.findall(r'([A-Z][a-z]*|[0-9])', equation, re.M)
for e in elements:
    print(e)
#separates the compound into individual elements
#I'm not sure how to apply the coefficients and subscripts to the elements

if elements 
    if there are the same number of elements on the left side:
        normal = leave the element right now
    else:
        balanced = set the amount elements on the right to equal to those on the left
#I think this is the main next step. This will probably be more than just a for and if/else code.

final = normal + balanced
#This is just putting the whole thing back together so that it looks like an equation again.

print "This is the balanced equation:" + final
#Finish

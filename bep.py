import re

equation = raw_input("Insert an equation:")

# Let us first split left and right side of equations, i.e. split them over '='
# sign.
split_over_equal = equation.split('=')
if len(split_over_equal) != 2 :
    raise ValueError("You didn't provide left-right side of the equation")

# variables to hold left and right side.
leftSide = None
rightSide = None
for index, side in enumerate(split_over_equal):
    # We split each compound in a dictionary object
    compositionAsDict = {}
    for compound in side.split('+'):
        # If we print compounds, we may still have spaces within the strings.
        # Those need not be removed here as regular expression below should
        # take are of that.
        # print("Compound: " + compound)

        # Regex doesn't support grouping into dictionary and searching repeatedly.
        # So search for the string, then zero it till we reach the end of
        # string.
        remaining = compound

        moleculeCount = 1
        while remaining:
            elements = re.search(r'(?P<Molecules_Count>[0-9])?(?:\s*)(?P<Element>[A-Z][a-z]*)(_(?P<Atoms_Count>[0-9]+))?(?:\s*)',
                    remaining, re.M)
            if elements.group('Molecules_Count'):
                moleculeCount = int(elements.group('Molecules_Count'))

            atomsCount = moleculeCount
            if elements.group('Atoms_Count'):
                atomsCount = int(elements.group('Atoms_Count'))
            if elements.group('Element') in compositionAsDict:
                compositionAsDict[elements.group('Element')] = compositionAsDict[elements.group('Element')]
            else:
                compositionAsDict[elements.group('Element')] = atomsCount
            remaining = remaining[elements.end():]
    if index == 0:
        leftSide = compositionAsDict
    else:
        rightSide = compositionAsDict

print "Initial left side of equation:"
print leftSide
print "Initial right side of equation:"
print rightSide

unmatchedItems = set(leftSide.keys()) ^ set(rightSide.keys())
if len(unmatchedItems):
    print("Following keys are only present on one-side of the equation")
    print " ".join(str(x) for x in unmatchedItems)
    raise ValueError("Can't balance equations due to unmatched elements")

# Now by definition we should have same keys (elements) on each side

for key in leftSide:
    if leftSide[key] < rightSide[key]:
        print("A number of atoms are different on the left and right side for Element " + "'" + key + "'")
        print("Balancing Element " + "'" + key + "'" + " on right side")
        leftSide[key] += 1
    elif leftSide[key] > rightSide[key]:
        rightSide[key] += 1

print "Final left side equation:"
print leftSide

print "Final right side equation:"
print rightSide

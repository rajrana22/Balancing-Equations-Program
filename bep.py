import re

equation = raw_input("Insert an equation:")


split_over_equal = equation.split("=")

print split_over_equal

for side in split_over_equal:

    for compound in side.split("+"):
        print("Compound: " + compound)
        compositionAsDict = {}
        remaining = compound

        moleculeCount = None
        while remaining:
            elements = re.search(r"(?P<Molecules_Count>[0-9])?(?:\s*)(?P<Element>[A-Z][a-z]*)(_(?P<Atoms_Count>[0-9]+))?(?:\s*)",
                    remaining, re.M)
            if not moleculeCount:
                moleculeCount = 1 if not elements.group("Molecules_Count") else int(elements.group("Molecules_Count"))

            atomsCount = 1 if not elements.group("Atoms_Count") else int(elements.group("Atoms_Count"))
            compositionAsDict[elements.group("Element")] = moleculeCount * atomsCount

            remaining = remaining[elements.end():]
        else:
            print compositionAsDict

for x in str.find(str(compositionAsDict),0,"="):
    compositionAsDictOnTheLeft = x

for y in str.find(str(compositionAsDict),"=", len(compositionAsDict)):
    compositionAsDictOnTheRight = y

if compositionAsDictOnTheLeft == compositionAsDictOnTheRight:

    print(userInput)

elif compositionAsDictOnTheRight > compositionAsDictOnTheLeft:
        compositionAsDictOnTheLeft += 1

else:
    while compositionAsDictOnTheLeft > compositionAsDictOnTheRight:
        compositionAsDictOnTheRight += 1

print compositionAsDictOnTheLeft + "=" + compositionAsDictOnTheRight

import re

equation = raw_input("Insert an equation:")


split_over_equal = equation.split("=")

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

left, right = split_over_equal

if left == right:

    print(equation)

elif right > left:
        left += 1

else:
    while left > right:
        right += 1

print left + "=" + right

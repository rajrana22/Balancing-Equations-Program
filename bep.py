import re
# @RAJ First the comments in the code are missing. You should insert what's the
# purpose of this code here including expected input, a new output and failure
# cases included some corner cases which really should be tested if needed.

# @RAJ Second your code was not really compiling. You have to put code in a source
# file in github not in a text document. So that all the code formatting stays.
# Read about how to use github.

# @RAJ I am creating some fictional elements He and Ol to check if my code works
# properly.
equation = "2 He_2 + Ol_2 + 2He_2Ol = 4  He_2Ol"


split_over_equal = equation.split('=')
# @RAJ Insert error if you get more than two elements or less than 2 elements.

for side in split_over_equal:
    # @RAJ insert logic to figure out if this is left side or right side
    # equation.

    for compound in side.split('+'):
        print("Compound: " + compound)
        compositionAsDict = {}
        remaining = compound

        moleculeCount = None
        while remaining:
            elements = re.search(r'(?P<Molecules_Count>[0-9])?(?:\s*)(?P<Element>[A-Z][a-z]*)(_(?P<Atoms_Count>[0-9]+))?(?:\s*)',
                    remaining, re.M)
            if not moleculeCount:
                moleculeCount = 1 if not elements.group('Molecules_Count') else int(elements.group('Molecules_Count'))

            atomsCount = 1 if not elements.group('Atoms_Count') else int(elements.group('Atoms_Count'))
            compositionAsDict[elements.group('Element')] = moleculeCount * atomsCount

            remaining = remaining[elements.end():]
        else:
            print compositionAsDict

            # @RAJ you want to decide what to do with this dictionary object.


# @RAJ you need to put logic for balancing. I did all the heavy lifting.

# @RAJ once you get it working, try removing _2 (i.e. subscripts) if you want
# to.

#  I on purpose removed all the comments from the code. Your task is to add extremely detailed comments on each and every line and send me the updated file.



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
# @NAVNEET no error, this variable splits the equation in two, splitting it from the equal sign.

for side in split_over_equal:
    # @RAJ insert logic to figure out if this is left side or right side
    # equation.
    # @NAVNEET isn't this both the left and the right sides? Because it splits it into two sides and the for loop takes both
    # right? I'm not sure what you are asking.

    for compound in side.split('+'):
        print("Compound: " + compound)
        compositionAsDict = {}
        remaining = compound
    # @NAVNEET first line splits each side into compounds by splitting from the plus sign.
    # Second line prints each compound. Third line is an empty dictionary, so you will use it later.
    # Fourth line is a variable you will use later as well, which contains each compound.

        moleculeCount = None
        while remaining:
            elements = re.search(r'(?P<Molecules_Count>[0-9])?(?:\s*)(?P<Element>[A-Z][a-z]*)(_(?P<Atoms_Count>[0-9]+))?(?:\s*)',
                    remaining, re.M)
            if not moleculeCount:
                moleculeCount = 1 if not elements.group('Molecules_Count') else int(elements.group('Molecules_Count'))
    # @NAVNEET You start on the first line by giving the variable "moleculeCount" no value.
    # Then the second line is a while loop for the compounds. The line after that defines an element, making the computer search
    # for it in the remaining variable, which are the compounds. It first groups the number of molecules, using [0-9] for it's
    # search parameters. It also indicates that there may not be a molecule count with the question mark after the group. The
    # next group is a non-capturing group, indicated by the "?:" in the beginning of the group. This makes it not remember the
    # matched text, because it is only a whitespace character. The next part is a group that searches for elements using both
    # capital and lowercase letters to search. The next group is the number of atoms, which is also searched through numbers,
    # and it may have more than one, represented with the "+", and it may not even exist, pepresented with the "?". Then there
    # is a non-capturing whitespace group again. The last line tells the computer that if there is no molecule count before an
    # element, we are assuming there's one there.

            atomsCount = 1 if not elements.group('Atoms_Count') else int(elements.group('Atoms_Count'))
            compositionAsDict[elements.group('Element')] = moleculeCount * atomsCount
    # @NAVNEET same with the first line here, if there is no atom count, then we are assuming there is a number one there. In the
    # second line, we go back to the "compositionAsDict" dictionary, and use it with every element in the compounds. This defines that
    # the number of elements are the number of molecules times the number of atoms, which is basically the coefficients times the
    # subscripts, which is how we will determine how much to add to balance the equation.
    
            remaining = remaining[elements.end():]
        else:
            print compositionAsDict
    # @NAVNEET I'm not sure what the "remaining = remaining[elements.end():]" line does, but you end the if/else statement in the
    # while loop with printing the "compositionAsDict" dictionary, giving the elements and their values.

            # @RAJ you want to decide what to do with this dictionary object.


# @RAJ you need to put logic for balancing. I did all the heavy lifting.

# @RAJ once you get it working, try removing _2 (i.e. subscripts) if you want
# to.

#  I on purpose removed all the comments from the code. Your task is to add extremely detailed comments on each and every line and send me the updated file.



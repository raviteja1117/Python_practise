"""
move = True
walk = False

if move and walk:
    print("It is monkey")
else:
    print("It is snake.")

move = False
walk = False


if move or walk:
    print("It is animal")
else:
    print("It is tree.")

move = True
walk = True
think = True
feel = True

if move and think and feel or walk:
    print("It is human")
else:
    print("It is not human.")


move = True
walk = True
think = True
feel = False

if (move and think and walk) and not feel:
    print("It is robot")
else:
    print("It is not not rebot.")
    """


def idenfify(walk= False, think= False, move=False, feel=False):
    if not walk and not think and not move and not feel:
        return "Tree"
    elif walk and not think and move and not feel:
        return "Monkey"
    elif walk and think and move and feel:
        return "Human"
    elif walk and think and move and not feel:
        return "Robot"
    else:
        return "This is invalid value"


# Tree
print("The searched species is", idenfify(walk= False, think= False, move= False, feel= False))
# Monkey
print("The searched species is", idenfify(walk= True, think= False, move=True, feel= False))
# Human
print("The searched species is", idenfify(walk= True, think= True, move=True, feel= True))
# Robot
print("The searched species is", idenfify(walk= True, think= True, move=True, feel= False))
#
print("The searched species is", idenfify(walk= True, think= True, move= False, feel= False))



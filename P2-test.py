partsOfQusCharms = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__"]
blanksOfCharms = "Alohomora,Lumos,Wingardium Leviosa,Protegos,Legilimens,Accio Firebolt,Nox"

qusOfCharms = ["You took your wand out and said __1__.",
               "In the darkness, you said __2__ and the wand was lit up.",
               "So you pointed it with your wand, saying __3__, and suddenly it floated up in the air. It was a flying broom.",
               "All of a sudden, you heard someone saying a curse at you in the darkness, so you shouted __4__, and the curse was rebound.",
               "The person fell down on the floor, so you approached him and accessed his mind by saying __5__.",
               "So you said __6__ to summon your broom and said __7__ to extinguish the light on the wand."]

ansOfcharmList = qusOfCharms[0].split()
print ansOfcharmList
print type(ansOfcharmList)

blanksOfCharmsList = blanksOfCharms.split()
print blanksOfCharmsList
print type(blanksOfCharmsList)

def word_in_pos(word, blanks):
    for pos in word:
        if pos in blanks:
            return pos
    return None


def play_game(ml_string, ansList):
    replaced = []
    # ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, ansList)
        if replacement != None:
            replaced.append("corgi,")
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced




print play_game(ansOfcharmList, partsOfQusCharms) #ansList is __1__, ml_string is ansOfcharmList

from random import randint
#i made it for 5 mines
def select(selection):
    while True:
        mine1 = randint(1 ,25)
        mine2 = randint(1 ,25)
        mine3 = randint(1 ,25)
        mine4 = randint(1 ,25)
        mine5 = randint(1 ,25)

        if mine1 == mine2:
            pass
        elif mine1 == mine3:
            pass
        elif mine1 == mine4:
            pass
        elif mine1 == mine5:
            pass
        elif mine2 == mine3:
            pass
        elif mine2 == mine4:
            pass
        elif mine2 == mine5:
            pass
        elif mine3 == mine4:
            pass
        elif mine3 == mine5:
            pass
        elif mine4 == mine5:
            pass
        elif mine1 == selection:
            pass
        elif mine2 == selection:
            pass
        elif mine3 == selection:
            pass
        elif mine4 == selection:
            pass
        elif mine5 == selection:
            pass
        else:
            break
    return(mine1, mine2, mine3, mine4, mine5)

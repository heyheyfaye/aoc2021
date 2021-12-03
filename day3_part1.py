gammarate = ""
epsilonrate = ""

with open("puzzle3.txt", "r") as inputPuzzle3:
    liste = [(line) for line in inputPuzzle3.read().split("\n")]

for x in range(len(liste[0])):
    one=0
    null=0

    for index, line in enumerate(liste):
        bit = line[x]

        if int(bit) == 1:
            one+=1
        elif int(bit) == 0:
            null+=1
        else:
            print("what's this?")
    
    if one > null:
        gammarate+=str(1)
        epsilonrate+=str(0)
    elif one < null:
        gammarate+=str(0)
        epsilonrate+=str(1)

print("\n gamma rate:", gammarate, "| gamma rate decimal:", int(gammarate,2),
"\n epsilon rate:", epsilonrate, "| epsilon rate decimal:", int(epsilonrate,2), 
"\n power:", int(gammarate,2)*int(epsilonrate,2))
with open("puzzle1.txt", "r") as inputPuzzle1:
    liste = [int(line) for line in inputPuzzle1.read().split("\n")]

increased = 0

for index, value in enumerate(liste[:len(liste)-3]):

    if (value+liste[index+1]+liste[index+2]) < (liste[index+1]+liste[index+2]+liste[index+3]):
        increased+=1

print("number of increases: ", increased)
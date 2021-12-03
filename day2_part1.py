import re 

with open("puzzle2.txt", "r") as inputPuzzle2:
    liste = inputPuzzle2.read().split("\n")

#print(liste)

horizontal = 0
depth = 0

for value in liste:
    if re.search('forward', value):
        number = re.search('[0-9]', value).group(0)
        horizontal+= int(number) 
    elif re.search('up', value):
        number = re.search('[0-9]', value).group(0)
        depth-= int(number)
    elif re.search('down', value):
        number = re.search('[0-9]', value).group(0)
        depth+= int(number)
    else:
        print("where are you going?")

print("final horizontal:", horizontal, "final depth:", depth, "answer:", horizontal*depth)
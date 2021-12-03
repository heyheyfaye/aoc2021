
with open("puzzle3.txt", "r") as inputPuzzle3:
    liste1 = [(line) for line in inputPuzzle3.read().split("\n")]

with open("puzzle3.txt", "r") as inputPuzzle3:
    liste2 = [(line) for line in inputPuzzle3.read().split("\n")]

#LISTE1 OXYGEN RATE
for x in range(len(liste1[0])):
    one=0
    null=0
    oxgen1=[]
    oxgen0=[]

    for index, line in enumerate(liste1):
        bit = line[x]

        if int(bit) == 1:
            one+=1
            oxgen1.append(line)
        elif int(bit) == 0:
            null+=1
            oxgen0.append(line)
        else:
            print("what's this?")

        #print("index:", x, "oxgen1:", oxgen1)
        #print("index:", x, "oxgen0:", oxgen0)
        
    if one > null:
        liste1 = oxgen1
        #print("one > null", liste1)
    elif one < null:
        liste1 = oxgen0
        #print("one < null", liste1)
    elif one == null:
        liste1 = oxgen1
        #print("one == null", liste1)
    else:
        print("something went wrong here")
        
    if len(liste1)==1:
        oxgenrate = liste1[0]
        break

#LISTE2 CO2 RATE
for x in range(len(liste2[0])):
    one=0
    null=0
    co2scrub1=[]
    co2scrub0=[]

    for index, line in enumerate(liste2):
        bit = line[x]

        if int(bit) == 1:
            one+=1
            co2scrub1.append(line)
        elif int(bit) == 0:
            null+=1
            co2scrub0.append(line)
        else:
            print("what's this?")

        #print("index:", x, "co2scrub1:", co2scrub1)
        #print("index:", x, "co2scrub0:", co2scrub0)
        
    if one > null:
        liste2 = co2scrub0
        #print("one > null", liste2)
    elif one < null:
        liste2 = co2scrub1
        #print("one < null", liste2)
    elif one == null:
        liste2 = co2scrub0
        #print("one == null", liste2)
    else:
        print("something went wrong here")
        
    if len(liste2)==1:
        co2scrubrate = liste2[0]
        break

print(
"\n oxygen generator rating:", oxgenrate, "| decimal:", int(oxgenrate,2),
"\n co2 scruber rating:", co2scrubrate, "| decimal:", int(co2scrubrate,2),
"\n result:", int(oxgenrate,2)*int(co2scrubrate,2)
)
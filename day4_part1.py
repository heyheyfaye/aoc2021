order = []
bingo = []

def markNumbers():
    for line in order:
        for indexmatrix, matrix in enumerate(bingo):
            for indexlines, lines in enumerate(bingo[indexmatrix]):
                for indexnumber, number in enumerate(bingo[indexmatrix][indexlines]):
                    if line == number:
                        bingo[indexmatrix][indexlines][indexnumber] = -1
        win = check()
        if not win == -999:
            return [win, line]


def createData():
    bingo=[]
    with open("puzzle4.txt","r") as file:
        order = file.readline().split(",")
        file.readline()
        for line in range(0,100):
            var = [[int(num) for num in file.readline().split()] for i in range(0,5)]
            bingo.append(var)
            file.readline()

    for i in range(0, len(order)):
        order[i] = order[i].replace("\n", "")
        order[i] = int(order[i])

    return [order, bingo]

def check():
    win = True
    for indexmatrix, matrix in enumerate(bingo):
        for indexlines, lines in enumerate(bingo[indexmatrix]):
            win = True
            for indexnumber, number in enumerate(bingo[indexmatrix][indexlines]):
                if number != -1:
                    win = False
            if win:
                return bingo[indexmatrix]
            
        for i in range (0,5):
            win = True
            for indexlines, lines in enumerate(bingo[indexmatrix]):
                if bingo[indexmatrix][indexlines][i] != -1:
                    win = False
            if win:
                return [bingo[indexmatrix]]
    return -999

def solution(data):
    win = data[0][0]
    print(win)
    factor = data[1]
    a=0
    for index, line in enumerate(win):
        for i in win[index]:
            if not i == -1:
                a=a+i
    return a*factor
                
                
order = createData()[0]
bingo = createData()[1]

print(solution(markNumbers()))

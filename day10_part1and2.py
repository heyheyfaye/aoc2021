import re

def read_input_original():
    with open("puzzle10.txt", "r") as input:
        list = [i for i in input.read().split("\n")]
    return list

def read_input_example():
    with open("example10.txt", "r") as input:
        list = [i for i in input.read().split("\n")]
    return list

def clean_text(rgx_list, text):
    new_text = text
    for rgx_match in rgx_list:
        new_text = re.sub(rgx_match, '', new_text)
    return new_text

#input = read_input_example()
input = read_input_original()

# search for REGEX "()" "[]" "<>" "{}" in line, than erase, so long as there a matches
# --> if everything is fine: all matches in the end
# --> if corrupted first closing character is causing the problem
# example: {([(<[} --> "}" first illegal character

#print(read_input_example())
characters_to_delete=["\\(\\)","\\[]","\\<>", "\\{\\}"]
#pattern = '[' + ''.join(characters_to_delete) + ']'
pattern = "\\(\\)|\\[]|\\<>|\\{\\}"
pattern2 = "\\)|\\]|\\>|\\}"
score=0
score2=0
solutions=[]

for i, row in enumerate(input):
    bool = ""
    while bool != None:
        #print(row)
        new_row=clean_text(characters_to_delete,row)
        #print("pattern:", pattern)
        bool = re.search(pattern, new_row)
        #print("new row:",i,new_row)
        #print("bool", bool)
        row=new_row

    if re.search(pattern2, row) == None:
        score2=0
        for char in reversed(row):
            score2=score2*5
            if char == "(":
                score2 += 1
            elif char == "[":
                score2 += 2
            elif char == "{":
                score2 += 3
            elif char == "<":
                score2 += 4
        solutions.append(score2)
          
    if re.search(pattern2, row) != None:
        bracket = re.search(pattern2, row).group(0)    
        if bracket == ")":
            score += 3
        elif bracket == "]":
            score += 57
        elif bracket == "}":
            score += 1197
        elif bracket == ">":
            score+= 25137

print("score:", score)
print("score2", sorted(solutions)[len(solutions)//2])
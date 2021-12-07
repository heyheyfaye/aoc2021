import numpy as np

def read_input_original():
    with open("puzzle7.txt", "r") as input:
        liste = [int(i) for i in input.read().split(",")]
    return liste

def read_input_example():
    with open("example7.txt", "r") as input:
        liste = [int(i) for i in input.read().split(",")]
    return liste

#input = read_input_example()
input = read_input_original()
print("input:", input)
fuel_list=[]

#maybe later: 
# - sort: most popular first
# - erase duplicates in list

for index, value in enumerate(input):
    diffsum=0
    for x in range(len(input)):
        diff = abs(value - input[x])

        #PART1: fuel consumption = steps to go 
        #diffsum = diff+diffsum

        #PART2: fuel consumption = sum of natural numbers 
        sumnatural=diff*(diff+1)/2
        
        diffsum = sumnatural+diffsum
    fuel_list.append(diffsum)
    
#print(fuel_list)
print("Fuel:", np.amin(fuel_list))
result = np.where(fuel_list == np.amin(fuel_list))
print('List of Indices of minimum element :', result[0])    
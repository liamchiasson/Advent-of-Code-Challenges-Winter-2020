#Advent of Code Problem, Day 1
# Find the two entries from the puzzle input that sum to 2020
# and then multiply those two numbers together.

entries = [] #to store the data on each line of the input file
f = open("input.txt") # open file
iteration = 0 #used to check iteration of loop
# (1) Fill list with input values:
while (f.closed != True): #while the file is open / isn't closed
    if(iteration == 0 or entries[iteration - 1] != ""): #if on first iteration or the last iteration was not an empty string
        entries.append(f.readline()) #read the next line and append it to entries[] list
        print (entries[iteration])
    elif entries[iteration - 1] == "":
        entries.pop() #remove last item in list if it was an empty string
        f.close()
    iteration += 1
#Typecast list elements from str to int
entries = list(map(int, entries))
# (2) Find the set of 2 numbers whose sum is 2020
num1 = 0 #first number of sum/product
num2 = 0 #second number of sum/product
num3 = 0 #third number of sum/product
for x in range(len(entries)):
    for y in range(len(entries) - 1):
        for z in range(len(entries) - 2):
            if ((entries[x] + entries[(y+1)] + entries[(z+2)]) == 2020):
                num1 = entries[x]
                num2 = entries[(y+1)]
                num3 = entries[(z+2)]
                break
        if(num1 > 0): break
    if (num1 > 0): break

# (3) Solution: Print Product
print (num1, num2, num3)
product = (num1 * num2 * num3)

print(product)

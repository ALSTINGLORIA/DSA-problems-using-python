array = [[1,2,-3],[7,2,-6],[-1,3],[4,7,-2,7],[3],[0,3]]
sum_array = []
sum = 0
for counter in range(len(array)):
    for counter2 in range(len(array[counter])):
        sum += array[counter][counter2]
    sum_array.append(sum)
    sum = 0
max = sum_array[0]
pointer = 0

for counter3 in range(len(sum_array)):
    if sum_array[counter3]>max:
        max = sum_array[counter3]
        pointer = counter3

print(max,"\t",array[pointer])
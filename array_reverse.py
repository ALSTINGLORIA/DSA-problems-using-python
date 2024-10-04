array = [1,2,3,4,5]
temp_array = []
print(array)

for counter in range(len(array)):
    temp_array.append(array[-(counter+1)])

array.clear
array = temp_array
print(array)
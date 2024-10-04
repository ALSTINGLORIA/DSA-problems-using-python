array1 = [1,4,7,3,2]
min = array1[0]
max = array1[0]
for counter in range(len(array1)):
    if(array1[counter]<min):
        min = array1[counter]
    

for counter in range(len(array1)):
    if(array1[counter]>max):
        max = array1[counter]


print("maximum element:",max)
print("minimum element:",min)
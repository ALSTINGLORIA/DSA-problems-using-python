array = [7,3,2,4,9,12,56]
counter1 = 0
counter2 = 0
flag = 0
while counter1 < (len(array)):
    min = array[counter1]
    while counter2 < len(array):
        if(min > array[counter2]):
            min = array[counter2]
            loc = counter2
            flag = 1
        counter2 += 1
    if(flag == 1):
        temp = array[counter1]
        array[counter1] = min
        array[loc] = temp
    counter1 += 1
    counter2 = counter1
    flag = 0


size = int(input("enter the size:"))
min_diff = array[size-1] - array[0]
print("the minimum difference is:",min_diff)

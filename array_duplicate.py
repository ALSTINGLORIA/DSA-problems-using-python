# Program checks if there is a duplicate element in the array
# True wll be printed if no duplicates, otherwise false
array = [1,5,7,3,8]
check = True
for counter in range(len(array)):
    number = array[counter]
    for counter2 in range(len(array)):

        if((number == array[counter2]) and (counter!=counter2)) :   # counter!=counter is given to not make it compare between the same item in the array 
            check = False
            break
    if(check == False):                     # to break out of the outer loop if check is false
        break

print(check)
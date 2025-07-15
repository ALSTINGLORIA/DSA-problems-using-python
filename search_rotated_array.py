nums = [4,5,6,7,0,1,2]

target = int(input("enter the target value:"))
start = 0
end = len(nums) - 1
while True:
    if start > end:
        print("target not found")
        break
    mid = (start + end) // 2
    if nums[mid] == target:
        print("target found at index:", mid)
        break
    else:
        if nums[mid]  >= nums[start]:
            if nums[start] <= target <= nums[mid]:
                end = mid-1
            else:
                start = mid +1
        else:
            if nums[end] >= target >= nums[mid]:
                start = mid+ 1
            else:
                end = mid-1

 


def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j

        temp =nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp

        print(nums)                 # to see how its swaping

nums = [5,7,9,3,4,6]
sort(nums)

print(nums)
print("BYE")

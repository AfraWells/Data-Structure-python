def BubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[i]
    return nums
nums=[1,2,54,654,2,324]
print(BubbleSort(nums))
def SortBucket(nums):
    max_num=max(nums)
    bucket=[0]*(max_num+1)
    for i in nums:
        bucket[i]+=1
    sort_nums=[]
    for j in range(len(bucket)):
        if bucket[j]!=0:
            sort_nums.append(j)
    return  sort_nums

nums=[1,43,45,2,5,6,7]
print(SortBucket(nums))
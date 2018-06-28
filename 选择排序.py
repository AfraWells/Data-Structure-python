def findsmallestnumber(arr):
    number=arr[0]
    index=0
    for i in range(len(arr)):
        if number>arr[i]:
            number=arr[i]
            index=i
    return index

def selectSort(arr):
    new_arr=[]
    for i in range(len(arr)):
        number=findsmallestnumber(arr)
        new_arr.append(arr.pop(number))
    return new_arr

print(selectSort([1,3,4,65,3,2,5]))

def binarySearch(arr,element):
    low = 0
    high = len(arr)-1
    mid = low+high//2

    while low <= high:
        if arr[mid] < element:
            mid = mid + 1
        elif arr[mid] > element:
            mid = mid - 1
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6]
b = binarySearch(arr,3)
if b:
    print("yes",b)
else:
    print("no")
def quicksort(arr,left,right):
    if left>=right:
        return
    start,end=left,right
    mid=(left+right)//2
    pivot=arr[mid]

    while start<=end:
        while arr[start]<pivot:
            start+=1

        while arr[end]>pivot:
            end-=1

        if start<=end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1

    quicksort(arr,left,end)
    quicksort(arr,start,right)

arr=[2,5,6,1,3]
print(arr)
quicksort(arr,0,len(arr)-1)
print(arr)




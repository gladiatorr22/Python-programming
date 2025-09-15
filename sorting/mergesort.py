def createlist():
    l1=[]
    while True:
        try:
            n=int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1
        
def merging(arr,left,mid,right):
    res=[]
    i=left
    j=mid+1
    while i<=mid and j<=right:
        if arr[i]<arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])
            j+=1
    #1st array extra values
    while i<=mid:
        res.append(arr[i])
        i+=1
    #2nd array extra values
    while j<=right:
        res.append(arr[j])
        j+=1
    #changes done on resultant should affect
    #original array
    for k in range(0,len(res)):
        arr[left]=res[k]
        left+=1

def mergesortbreaking(arr,left,right):
    if left==right:
        return
    mid=(left+right)//2 
    mergesortbreaking(arr, left, mid)
    mergesortbreaking(arr, mid+1, right)
    merging(arr, left, mid, right)
    return arr   

arr=createlist()
print("Unsorted array is: ", arr)
sorted_arr = mergesortbreaking(arr,left=0, right=len(arr)-1)
print("Sorted array is: ", sorted_arr)
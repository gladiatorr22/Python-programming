# wap to rotate the elements of given array to lhs for k no of times
def createlist():
    l1=[]
    while True:
        try:
            n=int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1
def reverse(arr,start, end):
    start=0
    end=len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def rotateleft(arr, k):
    n=len(arr)
    k=k%n
    if k == 0:
        return 
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)

arr=createlist()
k=int(input("enter the no of times to rotate the array: "))
rotateleft(arr, k)
print("Array after rotation:", arr)

    
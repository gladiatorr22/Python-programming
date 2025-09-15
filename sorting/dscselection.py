def createlist():
    l1=[]
    while True:
        try:
            n=int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1
def selectionsort(arr):
    n=len(arr) 
    for i in range(0,n-1):
        actualIndex=n-1-i
        min,currentminind=2**31,-1
        for j in range(0,n-i):
              if min>arr[j]:
                   min=arr[j]
                   currentminind=j
        arr[actualIndex],arr[currentminind] = arr[currentminind], arr[actualIndex]
    return arr            
arr=createlist()
res=selectionsort(arr)
print(res)
def createlist():
    l1=[]
    while True:
        try:
            n=int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1
def reverselist(arr):
    n=len(arr) 
    for i in range(0,n//2):
        arr[i],arr[n-1-i] = arr[n-1-i], arr[i]    
arr=createlist()
reverselist(arr)
print(arr)

def createlist():
    l1=[]
    while True:
        try:
            n=int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1
def secmax(nums):
    max,secmax=-2**31,-2**31
    maxind,secmaxind=-1,-1
    n=len(nums)
    for i in range(n):
        if nums[i]>max:
            secmax=max
            secmaxind=maxind
            max=nums[i]
            maxind=i
        elif max!=nums[i] and nums[i]>secmax:
            secmax=nums[i]
            secmaxind=i
    return secmax
nums=createlist()
res=secmax(nums)
print(f"{res} is the second maximum number in the list")
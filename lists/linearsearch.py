# def createlist():
#     l1=[]
#     while True:
#         try:
#             n= int(input("enter a number"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# nums=createlist()
# target=int(input("enter the target element to be searched"))
# flag,index = False,-1
# for i in range(0,len(nums)):
#     if target==nums[i]:
#         flag = True
#         index=i
#         break
# if flag==True:
#     print(f"my target is found at index:{index}")
# else:
#     print(f"{target} element not found")

# def createlist():
#     l1=[]
#     while True:
#         try:
#             n= int(input("enter a number:"))
#             l1.append(n)
#         except Exception as e:
#             return l1
        
# def linearsearch(nums,target):
#     for i in range(0,len(nums)):
#         if target==nums[i]:
#             return True,i
#     return False,-1

# nums=createlist()
# target=int(input("enter the target element to be searched:")) 
# flag,index=linearsearch(nums,target)

# if flag==True:
#         print(f"my target is found at index:{index}")
# else:
#         print(f"{target} element not found")   


def createlist():
    l1=[]
    while True:
        try:
            n= int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1
        
def find_max(nums):
    max=-2**31
    max_index=-1
    for i in range(0,len(nums)):
        if max<nums[i]:
            max=nums[i]
            max_index=i
    return max,max_index

def find_min(nums):
    min=2**31
    min_index=-1
    for i in range(0,len(nums)):
        if min>nums[i]:
            min=nums[i]
            min_index=i
    return min,min_index

nums=createlist()
max_value,max_index=find_max(nums)
min_value,min_index=find_min(nums)
print(f"maximum value={max_value} at index {max_index}")
print(f"maximum value={min_value} at index {min_index}")

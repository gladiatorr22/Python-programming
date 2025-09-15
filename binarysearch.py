# def createlist():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enter a number:"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# def binarysearch(nums,target):
#     left,right=0,len(nums)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return True, mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return False, -1
# nums = createlist()
# target = int(input("enter the target element to be searched: "))
# flag, index = binarysearch(nums, target)
# if flag:
#     print(f"target is found at index: {index}")  
# else:
#     print(f"{target} element not found")

# def createlist():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enter a number:"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# def binarysearchdesc(nums,target):
#     left,right=0,len(nums)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return True, mid
#         elif nums[mid] < target:
#             left = mid - 1
#             mid = (left + right) // 2
#         else:
#             right = mid + 1
#             mid = (left + right) // 2
#     return False, -1
# nums = createlist()
# target = int(input("enter the target element to be searched: "))
# flag, index = binarysearchdesc(nums, target)
# if flag:
#     print(f"target is found at index: {index}")  
# else:
#     print(f"{target} element not found")


def createlist():
    l1=[]
    while True:
        try:
            n=int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1
def orderagnosticbinarysearch(nums,target):
    left,right=0,len(nums)-1
    flag = True
    if nums[left] > nums[right]:
        flag = False
    while left <= right:
        mid = (left + right) // 2
        if flag:
            if nums[mid] == target:
                return True, mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[mid] == target:
                return True, mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return False, -1
nums = createlist()
target = int(input("enter the target element to be searched: "))
flags, index = orderagnosticbinarysearch(nums, target)
if flags==True:
    print(f"target is found at index: {index}")  
else:
    print(f"{target} element not found")
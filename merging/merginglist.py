'''using concatenate operator to merge two lists'''
# def createlist():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enter a number:"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# print("Enter elements for 1st array ")
# arr1=createlist()
# print("Enter elements for 2nd array")
# arr2=createlist()
# res=arr1+arr2
# print("Merged array is : ",res)

'''using extend method to merge two lists'''
# def createlist():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enter a number:"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# print("Enter elements for 1st array ")
# arr1=createlist()
# print("Enter elements for 2nd array")
# arr2=createlist()
# arr1.extend(arr2)
# print("Merged array is : ",arr1)

'''using for loop to merge two lists'''
# def createlist():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enter a number:"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# print("Enter elements for 1st array ")
# arr1=createlist()   
# print("Enter elements for 2nd array")
# arr2=createlist()
# for i in arr2:
#     arr1.append(i)
# print("Merged array is : ",arr1)

'''using insert method to merge two lists '''
# def createlist():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enter a number:"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# print("Enter elements for 1st array ")
# arr1=createlist()
# print("Enter elements for 2nd array")
# arr2=createlist()
# for i in arr2:
#     arr1.insert(len(arr1),i)
# print("Merged array is : ",arr1)

'''write the prgram to merge the given two ascending sorted array in ascending order'''
def createlist():
    l1=[]
    while True:
        try:
            n=int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1
print("Enter elements for 1st array ")
arr1=createlist()
print("Enter elements for 2nd array")
arr2=createlist()
def mergeasc(arr1,arr2):
    res=[]
    i,j=0,0
    n1,n2=len(arr1),len(arr2)
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<n1:
        res.append(arr1[i])
        i+=1
    while j<n2:
        res.append(arr2[j])
        j+=1
    return res
res=mergeasc(arr1,arr2)
print(res)
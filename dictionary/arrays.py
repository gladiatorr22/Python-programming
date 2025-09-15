# wap to display the following of a given arrray
# a. duplicates of a given array
# b. unique elements of a given array
# c. non duplicates of a given array

# duplicates => repeated elements in the array
# unique => elements that occur exactly once in the array 
# non duplicates => elements that occur atleast once in the array  

def createlist():
    l1=[]
    while True:
        try:
            n= int(input("enter a number:"))
            l1.append(n)
        except Exception as e:
            return l1

def duplicates(arr):
    dict = {}
    for i in range(0,len(arr)):
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1
    dup=[]
    uni=[]
    non_dup=[]
    for key, val in dict.items():
        
        if val > 1:
            dup.append(key)
        if val == 1:
            uni.append(key)
        if val >= 1:
            non_dup.append(key)
    return dup, uni, non_dup

arr=createlist()
dup,uni,non_dup=duplicates(arr)
print(f"duplicates: {dup}")
print(f"unique elements: {uni}")
print(f"non duplicates: {non_dup}")

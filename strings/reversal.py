'''decrementing for loop'''

# def decrreversal(str1):
#     nstr=""
#     for i in range(len(str1)-1,0-1,-1):
#         nstr=nstr+str1[i]
#     return nstr

# str1=input("enter a string: ")
# res=decrreversal(str1)
# print(str1)
# print(res)

'''incrementing for loop'''

# def increreversal(str1):
#     nstr=""
#     for i in range(0,len(str1)):
#         nstr=str1[i]+nstr
#     return nstr

# str1=input("enter a string: ")
# res=increreversal(str1)
# print(str1)
# print(res)

'''decr reversal using recursion'''

# def decrreversal(str1,nstr,i):
#     if i<0:
#         return nstr
#     nstr=nstr+str1[i]
#     return decrreversal(str1,nstr,(i-1))


# str1=input("enter a string: ")
# res=decrreversal(str1,"",len(str1)-1)
# print(str1)
# print(res)

'''incr reversal using recursion'''

# def decrreversal(str1,nstr,i):
#     if i>=len(str1):
#         return nstr
#     nstr=str1[i]+nstr
#     return decrreversal(str1,nstr,(i+1))


# str1=input("enter a string: ")
# res=decrreversal(str1,"",0)
# print(str1)
# print(res)


''' string reversal using list '''

def stringreversal(str):
    l1=[]
    for i in str:
        l1.append(i)
    
    i,j=0,len(l1)-1
    while i<j:
        l1[i],l1[j]=l1[j],l1[i]
        j-=1
        i+=1

    nstr=""
    for i in l1:
        nstr=nstr+i

    return nstr

str=input("enter a string: ")
res=stringreversal(str)
print(str)
print(res)

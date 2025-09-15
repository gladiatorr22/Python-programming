# l1=[]
# while True:
#     try:
#         n=int(input("enter a number:"))
#         l1.append(n)
#     except Exception as e:
#         break
# print(l1)

# def createlist():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enter a number:"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# res=createlist()
# print(res)
def createlist():
    l1=[]
    while True:
            n=input("enter a character:")
            if n=="":
                return l1
            l1.append(n)
res=createlist()
print(res)
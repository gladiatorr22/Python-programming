def anagramfiltrations(s):  
    filtered = ""
    for char in s:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122: 
            filtered += char
        elif 65 <= ascii_val <= 90: 
            filtered += chr(ascii_val + 32)  
    return filtered


# def isanagrams(s1,s2):
#     s1=anagramfiltrations(s1)
#     s2=anagramfiltrations(s2)
#     if len(s1)!=len(s2):
#         return False
#     else:
#         ascii=[0]*26
#         for i in range(len(s1)):
#             ascii[ord(s1[i])-97]+=1
#             ascii[ord(s2[i])-97]-=1
#         print(ascii)
#         for i in range(len(s1)):
#             if i!=0:
#                 return False
#             else:
#                 return True

def isanagrams(s1, s2):
    s1 = anagramfiltrations(s1)
    s2 = anagramfiltrations(s2)
    if len(s1) != len(s2):
        return False
    else:
        dict = {}
        for i in range(len(s1)):
            if s1[i] in dict:
                dict[s1[i]] = dict[s1[i]] + 1
            else:
                dict[s1[i]] = 1

            if s2[i] in dict:
                dict[s2[i]] = dict[s2[i]] - 1
            else:
                dict[s2[i]] = -1

        print(dict)

        for key, val in dict.items():
            if val != 0:
                return False
        return True

s1 = input("Enter first string: ")
s2 = input("Enter second string: ") 
flag= isanagrams(s1, s2)
if flag:
    print("Strings are anagrams")   
else:
    print("Strings are not anagrams")
    
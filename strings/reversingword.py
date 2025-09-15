def reversal(str):
    i=0
    str=str+" "
    nwrd=""
    nsen=""
    while i < len(str):
        if str[i]!=" ":
            nwrd=str[i]+nwrd
        elif nwrd!="":
            if nsen=="":
                nsen=nsen+nwrd
            else:
                nsen=nsen+" "+nwrd
            nwrd=""
        i+=1
    return nsen
        
str=input("enter a string: ")
res=reversal(str)
print(res)

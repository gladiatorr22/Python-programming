n=int(input("enter a number : "))
incre=1
decre=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2!=0:
            print(incre,end=" ")
            decre=incre
        else:
            print(decre,end=" ")
            decre-=1
        incre+=1
    print()
    decre=decre+n
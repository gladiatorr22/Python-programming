try:
    val=int(input("enter a number"))
    print(val)
    print(type(val))
except Exception as e:
    print("invalid input")
x=int(input("Enter temp:"))
if x<0:
    print("Freezing")
elif x>0 and x<20:
    print("Cold")
elif x>21 and x<=35:
    print("Warm")
else:
    print("Hot")
num1, num2, num3 = map(int, input("Enter three number(by one line) : ").split())

if num1 > num2:
    print("Big number : ",num1)
elif num2 > num1:
    print("Big number : ",num2)    
elif num2 > num3:
    print("Big number : ",num2)
elif num3 > num2:
    print("Big number : ",num3)
elif num1 > num3:
    print("Big number : ",num1)        


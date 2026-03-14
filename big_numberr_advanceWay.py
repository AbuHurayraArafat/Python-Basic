num1, num2, num3 = map(int,input("Enter three number : ").split())

big = num1

if num2 > big:
    big = num2
elif num3 > big:
    big = num3

print ("Big Number : ",big)        

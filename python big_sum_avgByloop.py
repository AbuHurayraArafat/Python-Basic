numbers = input("Enter numbers separated by space (max 4):").split()

while len(numbers) > 4:
    print ("To many numbers maximum 4 number allowed")
    numbers = input("Enter numbers again : ").split()

numbers = list(map(int, numbers))    

biggest = max(numbers)
smallest = min(numbers)
total = sum(numbers)
average = total/len(numbers)

print("Big number is      : ",biggest)
print("Smallest number is :",smallest)
print("Sum of every number:",total)
print("Average is         :",average)

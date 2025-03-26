number = int(input("enter the number : "))
if number < 0 :
    print("Enter the positive number")
    exit()

factorial = 1

while number > 0 :
    factorial *= number
    number -= 1

print(factorial)
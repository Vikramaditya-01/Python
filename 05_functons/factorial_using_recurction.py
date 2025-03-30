number = int(input("Enter the number : "))

#  using simple loop
def factorial(num):
    value = 1
    for i in range(1 , num+1):
        value *= i
    return value

result = factorial(number)
print(result)

# using recursive function
def factorial(n):
    if n == 0:
        return 1
    else :
        return n * factorial(n-1)
    
recursive_result = factorial(number)
print(recursive_result)

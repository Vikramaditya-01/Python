number = int(input("Enter the number : "))
is_Prime = True

if number > 1 :
    for i in range(2 , number) :
        if (number % i) == 0 :
            is_Prime = False
            break


elif number == 1 :
    print ("1 is not prime Number ")
else :
    print("Not a prime Number")
    exit()

print(is_Prime)

        
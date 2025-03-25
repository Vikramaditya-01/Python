Number = int(input("Enter your Score For Calculate Your Grade : "))

if Number >= 101:
    print("Verify Your Number . It's Should Be in Between 1 - 100 ")
    exit()

if Number >=90:
    print("Your Grade is A ")

elif Number >=80:
    print("Your Score is B")

elif Number >=70:
    print("Your Score is C")

elif Number >=60:
    print("Your Score is D")

else:
    print("Your Score is F")


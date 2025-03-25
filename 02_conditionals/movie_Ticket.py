User_age = int(input("Enter your age: "))
Movie_day = input("Enter todays day in word : ")


Price = 12 if User_age >= 18 else 8

if Movie_day.upper() == "WEDNESDAY":
    print("Yea! You got an discount of $2 . and Your Total Bill For movie Ticket Will be $", Price-2)

else:
    print("Your Total Bill for Movie Ticket is $", Price)  



  
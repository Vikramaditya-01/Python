pet = input("Enter your pet's name : cat or dog : ")
age = int(input("enter the age of your pet "))

if age < 0 :
    print("age cannot be negative")
    exit()

if pet.upper() == "CAT" :
    print("senior cat food") if age >5 else print("junior cat food")
elif pet.upper() == "DOG" :
    print("puppy food ") if age < 2 else print("adult dog food")
else:
    print("choose the right inputs")
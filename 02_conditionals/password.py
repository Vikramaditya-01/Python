password = input("Enter your password : ")
length = len(password)

if length < 6 :
    print("weak password")
elif length <= 10 :
    print("Medium password")
else:
    print("strong password")
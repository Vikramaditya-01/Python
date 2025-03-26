number = int(input("Enter the number for which you need table : "))

for i in range(1 , 11) :
    if i == 5 :
        continue
    else :
        print(number , "X" , i , "=" , number*i)
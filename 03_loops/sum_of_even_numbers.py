Given_number_by_user = int(input("Enter the number for finding the sum of all even number from zero : "))
sum_of_all_even_number = 0

if Given_number_by_user == 0 or Given_number_by_user < 0 :
    print("enter the positive numbers")
    exit()
    
for number in range( 1 , Given_number_by_user+1) :
    if number % 2 == 0:
        sum_of_all_even_number += number

print(sum_of_all_even_number)
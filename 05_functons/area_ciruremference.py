import math
user_input_of_radius = int(input("Enter the Radius of the circle : "))

def area(num):
    area = math.pi * num ** 2
    circumference = 2 * math.pi * num
    return area , circumference

ar , cir = area(user_input_of_radius)
print("Area : ", ar , " :: circumference : " , cir) 
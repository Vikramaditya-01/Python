fruit = "Banana"
color = input("Enter the color for your fruit Green  ; Yellow  ; brown  : ")

if fruit == "Banana":
    if color.upper() == "GREEN":
        print("your Banana is Unripe")
    elif color.upper() == "YELLOW":
        print("your Banana is Ripe")
    elif color.upper() == "BROWN":
        print("your Banana is overripe")
    else:
        print("Choose the correct color and input ")
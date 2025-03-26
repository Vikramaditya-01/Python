string_input = input("Enter the string : ")

for char in string_input :
    print(char)
    if string_input.count(char) == 1 :
        print(char)
        break
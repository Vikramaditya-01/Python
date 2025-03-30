NUMBERS = map(int,input("Enter The numbers : ").split()) # NUMBERS is a map object 
def sum_all(*args):
    return sum(args)


result = sum_all(*NUMBERS)   # as it is a map object we  need to unpack it for that here we have used *  . either it will show error because in the function permeter *args expects multiple individual values,not one object.
print(result)
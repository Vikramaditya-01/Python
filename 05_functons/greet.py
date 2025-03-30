name = input("Enter Your Name : ") or "World"

def greet(name):
    return "Hello " + name

greeted = greet(name)
print(greeted)
import time 

def timer(function):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__} ran in {end - start}")
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)

example_function(2)
# @f: Function
# @return wrapper:  Modified version of a function
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper


@announce  # Add the announce decorator to the hello() function
def hello():
    print("Hello, world!")


# Call of the function
hello()

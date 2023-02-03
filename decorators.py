# function that takes a function as input and modifies another function

def announce(baseFunction):
    # wrapper will announce a message before executing function then execute, then announce function was executed
    def wrapper():
        print('About to run a function')
        baseFunction()
        print('Done with the function.')
    return wrapper


@announce  # will add the decorators to this function
def hello():
    print('hello, world!')


hello()

# => output
# hello, world!
# Done with the function.

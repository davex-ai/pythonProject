

def logtime(func):
    def wrapper():
        print("then")
        val = func()
        print("now")
        return
    return wrapper

@logtime
def hello():
    print("hello")
hello()
try:
    print(2/0)
except ZeroDivisionError:
    print("Cant divided by 0 error")
finally:
    print("THis is a finally block")

try:
    raise Exception("Intentional Error")
except Exception as error:
    print(error)
    print("This is a general exception block")

class PythonError(Exception):
    print("Dummy Error Class")
    pass

try:
    raise PythonError()
except PythonError:
    print("Caught the error")
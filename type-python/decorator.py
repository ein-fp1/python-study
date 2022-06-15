def decorator(func):
    def new_func():
        print("Hi")
        func()

    return new_func


@decorator
def smile():
    print("😀")


@decorator
def angry():
    print("😠")


@decorator
def love():
    print("😍")


smile()
angry()
love()

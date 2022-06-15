def decorator(func):
    def new_func():
        print("Hi")
        func()

    return new_func


def smile():
    print("😀")


def angry():
    print("😠")


def love():
    print("😍")


smile = decorator(smile)
angry = decorator(angry)
love = decorator(love)

smile()
angry()
love()

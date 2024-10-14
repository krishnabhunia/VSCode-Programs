x = "1"
y = "1"

print(x, y)


def myfunc():
    # global x
    # global y
    # print("myfunc before",x,y)
    y = "2"
    x = "2"
    print("myfunc after", x, y)


def myfunc1():
    global x
    global y
    print("myfunc1 before", x, y)
    y = "3"
    x = "3"
    print("myfunc1 after", x, y)


myfunc()
myfunc1()

print("Python is " + x, y)

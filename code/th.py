import threading

mydata = "currently none"


def t1(d1):
    global mydata
    print("In t1 function:", d1, mydata)
    mydata = d1
    print("data modified", d1, mydata)


def t2(d2):
    global mydata
    print("In t1 function:", d2, mydata)
    mydata = d2
    print("data modified", d2, mydata)


def t3():
    try:
        th1 = threading.Thread(target=t1, name="krishna", args=("krishna data",))
        print("thread starting")
        th1.start()
        print("thread started, and will run")
        th1.join(timeout=5)
        print("thread joined and killed")

        th2 = threading.Thread(target=t2, name="dipayan", args=("dipayan data",))
        print("thread starting")
        th2.start()
        print("thread started, and will run")
        th2.join(timeout=5)
        print("thread joined and killed")

        print("my data is", mydata)

    except Exception as ex:
        print("Error occured ", ex)


t3()

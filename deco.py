def wish(wishmain):
    def proc(*args,**kwargs):
        # print(args,kwargs)
        print(f"Good {args[0]}")
        wishmain(kwargs['firstname'],kwargs['secondname'])
        print(f"Thank you {args[1]}")
    return proc

@wish
def wishmain(firstname = "No first name", secondname = "No second name"):
    print(f"Wishing {firstname} and {secondname}")

wishmain(firstname = "Krishna",secondname = "Bhunia")

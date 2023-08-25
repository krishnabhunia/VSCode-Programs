def wish(func):
    def proc(*args,**kwargs):
        print("")
        if len(args) == 2 and len(kwargs)==2:
            print(f"Good {args[0]}")
            func(kwargs['firstname'],kwargs['secondname'])
            print(f"Thank you {args[1]}")
        else:
            if len(args) == 2:
                func(args[0],args[1])
            elif len(kwargs) == 2:
                func(kwargs['firstname'],kwargs['secondname'])
            else:
                print("InAppropiate arguements")
                func("No One")
    return proc

@wish
def wishmain(firstname="No first name", secondname="No second name"):
    print(f"Wishing {firstname} {secondname}")

wishmain("Morning","Sir",firstname = "Krishna", secondname = "Bhunia")
wishmain("Morning",firstname = "Krishna", secondname = "Bhunia")
wishmain(secondname = "Bhunia",firstname = "Krishna")
wishmain("ok")
wishmain("Krishna","Bhunia")

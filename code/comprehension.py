def checkEvenOdd(x): return "Even" if x % 2 == 0 else "Odd"


print(checkEvenOdd(10.5))
l = [checkEvenOdd(i) for i in range(10)]
print(l, type(l))
s = (checkEvenOdd(i) for i in range(10))
print(s, type(s))  # this is generator
t = {checkEvenOdd(i): i for i in range(10)}
print(t, type(t))

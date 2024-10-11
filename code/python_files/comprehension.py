def checkEvenOdd(x): return "Even" if x % 2 == 0 else "Odd"


print(checkEvenOdd(10.5))
return_list = [checkEvenOdd(i) for i in range(10)]
print(return_list, type(return_list))
generator_obj = (checkEvenOdd(i) for i in range(10))
print(generator_obj, type(generator_obj))  # this is generator
dictionary = {checkEvenOdd(i): i for i in range(10)}
print(dictionary, type(dictionary))

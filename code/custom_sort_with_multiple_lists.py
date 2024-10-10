import re

r = []
def check_lst(lst):
    if type(lst) == list:
        for i in lst:
            if type(i) == list:
                check_lst(i)
            else:
                r.append(i)

inp = ["Sam", [10.987, [2.0, ["Hi", 39]], "Hello12345"], [[[56, 10.345678, ["He!!0"]]]]]

check_lst(inp)
print(inp)
print(r)

def my_sort(x):
    if isinstance(x, str) and x.isalnum():
        return (1, x)  # Numbers get category 0
    elif isinstance(x, str):
        return (0, x)  # Alphanumerics get category 1
    elif isinstance(x, int):
        return (2, x)  # Pure strings get category 2
    elif isinstance(x, float):
        return (3, x)  # Pure strings get category 2
    
s = sorted(r, key=my_sort)
print(s)

# ['Hi', 'Sam', 'He!!0', 'Hello12345', 39, 56, 2.0, 10.345678, 10.987]

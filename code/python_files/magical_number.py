# import random

# n = random.randint(1000, 9999)
# print(n)
d = {}
dnot = {}
for i in range(1000, 9998):
    # Convert number to string, pad with leading zeros if necessary
    interations = 0
    n = i
    print(n)
    while n != 6174:
        num_str = str(n).zfill(4)

        # Sort the digits in descending and ascending order
        largest = int("".join(sorted(num_str, reverse=True)))
        smallest = int("".join(sorted(num_str)))

        # Perform subtraction
        n = largest - smallest
        interations += 1
        print(f"Iteration {interations} with number {largest} - {smallest} = {n} for {i}")

        if n == 6174:
            d[i] = interations
            break
        if interations > 9999:
            dnot[i] = interations
            break
       
    
res = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(res[0])
print(res[-1])
print(dnot)

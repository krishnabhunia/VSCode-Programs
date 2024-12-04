inp = 'aaabcdefghaannpouiytrewsdrtgft'
char_ind = {}
first = 0
maxlen = 0
maxstr = ''
for last in range(len(inp)):
    if inp[last] in char_ind and char_ind[inp[last]] >= first:
        first = char_ind[inp[last]] + 1
    char_ind[inp[last]] = last
    
    if maxlen < last - first + 1:
        maxlen = last - first + 1
        maxstr = inp[first:last+1]

print(f"The max string is : '{maxstr}' having len : {maxlen}")
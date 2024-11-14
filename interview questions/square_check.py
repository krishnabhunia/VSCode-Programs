inp = [1,2,3,4]
sq = [16,1,9,4]

for i in inp:
    if i**2 in sq:
        print(i,"present")
    else:
        print(i,"not present")

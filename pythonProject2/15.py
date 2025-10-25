p = list(range(25,65))
q = list(range(40,116))
a = []
for x in range(1,1000):
    if (x in p) <= (( x in q) and not(x in a)) <= (not(x in p )) == False:
        a.append(x)
print(a)
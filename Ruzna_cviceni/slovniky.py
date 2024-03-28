slovnik = {0:10000}

for x in range (0,10):
    slovnik[x] = slovnik.get(x,x+1)
    print(f"{slovnik[x]=}")

print(slovnik)

for k,v in slovnik.items():
    print(f"{k=} {v=}")

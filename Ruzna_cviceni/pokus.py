byci = 0
kravy = 0

hrac = "1234"
pocitac = "5201"

"""for a in hrac:
    for b in pocitac:
        if a == b:
            if pocitac.index(b) == hrac.index(a):
                byci += 1
            else:
                kravy += 1"""

for x in range(len(hrac)):
    print(f"{x=}")
    if hrac[x] == pocitac[x]:
        byci +=1
    elif hrac[x] in pocitac:
        kravy +=1

print(f"{byci=}{kravy=}")
#byci = sum(s == g for s, g in zip(pocitac, hrac))
#kravy = sum(min(hrac.count(x), pocitac.count(x)) for x in set(hrac)) - byci
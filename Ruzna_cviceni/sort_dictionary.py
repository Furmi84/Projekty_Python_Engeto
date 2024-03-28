myDict = {'e': 10, 'b': 9,
		'c': 15, 'a': 2, 'd': 32}

#myKeys = list(myDict.keys())
#myKeys.sort()
#sorted_dict = {i: myDict[i] for i in myKeys}

#print(sorted_dict)
for k,v in myDict.items():
    print(f"{k=}{v=}")

print("-"*20)
for k,v in sorted(myDict.items()):
    print(f"{k=}{v=}")

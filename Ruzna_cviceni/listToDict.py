# Seznam klíčů
klice = ['klic1', 'klic2', 'klic3']

# Seznam hodnot
hodnoty_1 = [1, 2, 3]
hodnoty_2 = [3, 4, 5]

# Vytvoření slovníku z obou seznamů
slovnik = {klice[i]:[hodnoty_1[i], hodnoty_2[i]] for i in range(len(klice))}

# Výpis vytvořeného slovníku
print(slovnik)
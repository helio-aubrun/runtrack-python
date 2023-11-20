inventaire= {"nom":"carte", "prix":10, "nb":100}
print(f"{inventaire["nom"]}, {inventaire["prix"]}€, en stock : {inventaire["nb"]}")
choix=int(input("combein voulez-vous en prendre : "))
inventaire["nb"] = inventaire["nb"] - choix
inventaire["prix"] = inventaire["prix"] + ((inventaire["prix"] // 100) * 10)
print(f"{inventaire["nom"]}, {inventaire["prix"]}€, en stock : {inventaire["nb"]}")
def my_sort(lst):
    sorted = False
    total_swaps = 0
    while not sorted:
        swaps = 0
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swaps += 1
        total_swaps += swaps
        if swaps == 0:
            sorted = True
    print("Nombre total de coups nécessaires pour trier la liste :", total_swaps)
    return lst

ma_liste = [5, 2, 9, 1, 5, 6]
liste_triee = my_sort(ma_liste)
print("Liste triée :", liste_triee)
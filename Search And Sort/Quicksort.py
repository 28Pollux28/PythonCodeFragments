def quicksort(tab):
    if len(tab) <= 1:
        return tab
    else:
        return quicksort([y for y in tab[1:] if y < tab[0]])
        + [tab[0]]
        + quicksort([y for y in tab[1:] if y >= tab[0]])
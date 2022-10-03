def fibonnacci(n):
    n0 = 0
    n1 = 1
    for i in range(2,n):
        suivant = n0+n1
        n0 = n1
        n1 = suivant
    return n1
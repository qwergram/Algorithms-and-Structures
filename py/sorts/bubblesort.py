def bubblesort(l):
    for i in range(0, len(l)-1):
        for i in range(1, len(l)):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
    return l
def bubblesort(l):
    last = l[:]
    for i in range(0, len(l))-1):
        for i in range(1, len(l)):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
        if last != l:
            last = l[:]
        else:
            break
    return l
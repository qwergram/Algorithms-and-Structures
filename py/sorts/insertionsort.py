def insertionsort(values):
    if len(values) > 1:
        for j in range(len(values) - 1):
            for i in range(1, len(values)):
                if values[i] < values[i - 1]:
                    values[i], values[i-1] = values[i-1], values[i]
    return values
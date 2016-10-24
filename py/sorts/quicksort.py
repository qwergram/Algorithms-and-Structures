# A quicksort
# https://en.wikipedia.org/wiki/Quicksort


def recursiveQuicksort(values):
    if values:
        pivot, smaller, larger = values[0], [], []
        for item in values[1:]:
            if item < pivot:
                smaller.append(item)
            else:
                larger.append(item)
        return recursiveQuicksort(smaller) + [pivot] + recursiveQuicksort(larger)
    return values
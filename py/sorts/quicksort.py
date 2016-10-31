# A quicksort
# https://en.wikipedia.org/wiki/Quicksort

# According to MS, this is wrong
# According to the Python Community, this is right
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


# According to MS, this is right
# According to the Python Community, this is okay
# However it reeks of C
def inplaceQuicksort(values, begin=0, end=None):
    def partition(array, begin, end):
        pivot = begin
        for i in range(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
        array[pivot], array[begin] = array[begin], array[pivot]
        return pivot
    end = len(values) - 1 if end is None else end
    if begin >= end: return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

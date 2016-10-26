# A mergesort

def mergesort(values):
    if len(values) > 1:
        first_half, second_half, result = mergesort(values[:len(values)//2]), mergesort(values[len(values)//2:]), []
        while first_half or second_half:
            if not first_half and second_half:
                result.append(second_half.pop(0))
            elif not second_half and first_half:
                result.append(first_half.pop(0))
            elif first_half[0] < second_half[0]:
                result.append(first_half.pop(0))
            else:
                result.append(second_half.pop(0))            
        return result
    return values


assert mergesort([]) == []
assert mergesort([1]) == [1], mergesort([1])
assert mergesort([1,2,3]) == [1,2,3], mergesort([1,2,3])
assert mergesort([3,2,1]) == [1,2,3]
assert mergesort([3,6,3,8,9,1,4]) == [1,3,3,4,6,8,9]
assert mergesort([3,1,5]) == [1,3,5]
assert mergesort([]) == []
assert mergesort([2,1]) == [1,2]
assert mergesort([2,1,1]) == [1,1,2]
assert mergesort([2,1,1,2,5]) == [1,1,2,2,5]
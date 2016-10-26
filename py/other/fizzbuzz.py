def fizzbuzz(array):
    for item in array:
        result = ""
        if item % 3 == 0:
            result += "fizz"
        if item % 5 == 0:
            result += "buzz"
        print(result or item) 
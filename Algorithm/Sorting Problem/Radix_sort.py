def countSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(array):
    """radixSort
    from least import digit to most significant digit
    every digit using countsort"""
    max1 = max(array)
    exp = 1
    while max1 // exp > 0:
        countSort(array, exp)
        exp *= 10
    return array

if __name__ == "__main__":
    array = [170, 45, 75, 90, 802, 24, 2, 66]
    sortarray = radixSort(array)
    print(sortarray)
    
import random

def parpartition(array, start, end):
    pivot = start
    # pivot = random.choice(range(len(array)))
    # generate random pivot, so make expected running time <= O(nlogn)
    for i in range(start+1, end):
        if array[i] <= array[pivot]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[start], array[pivot] = array[pivot], array[start]
    return pivot

def Quick_sort(array, start, end=None):
    if end == None:
        end = len(array)
    if start < end:   
        pivot = parpartition(array, start, end)
        Quick_sort(array, start, pivot)
        Quick_sort(array, pivot+1, end)


if __name__ == "__main__":
    arr = [100, 107, 101, 200, 211, 97]
    Quick_sort(arr,0)
    print(arr)


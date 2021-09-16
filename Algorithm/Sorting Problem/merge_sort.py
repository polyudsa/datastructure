def merge(left, right):
    """
    merge——subroutine
    """
    temp_list = []
    while len(left) > 0 and len(right) > 0:
        # x = left.pop(0)
        # y = right.pop(0)
        # 没合并前不能少元素，所以上面两个有问题
        if left[0] < right[0]:
            temp_list.append(left.pop(0))
        else:
            temp_list.append(right.pop(0))
    temp_list += right
    temp_list += left
    return temp_list

def merge_sorted(arr):
    """
    merge_sort:recursive sorting
    """
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    left = arr[:m]
    right = arr[m:]
    return merge(merge_sorted(left), merge_sorted(right))

if __name__ == '__main__':
    test_list = [9, 1, 3, 5, 18, 7]
    test_list = merge_sorted(test_list)
    print(test_list)
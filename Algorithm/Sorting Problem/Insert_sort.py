def insert_sort(lists):
    """input: unordered lists
       output: ordered lists 
    """
    for i in range(1, len(lists)):
        key = lists[i]
        j = i - 1
        while j >= 0  and lists[j] > key:
            # 这里不能用 lists[i] 因为原位置元素发生变化了
            lists[j+1] = lists[j]
            j -= 1
        lists[j + 1] = key
    return lists
    
if __name__ == "__main__":
    lists = [2, 8, 9, 1, 6, 7]
    print(insert_sort(lists))

        

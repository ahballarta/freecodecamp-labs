def quick_sort(array):
    n = len(array)
    if n == 0:
        return []
    pivot = array[0]
    lesser_sublist = []
    equal_sublist = []
    greater_sublist = []
    for i in range(n):
        if pivot == array[i]:
            equal_sublist.append(array[i])
        if pivot > array[i]:
            lesser_sublist.append(array[i])
        if pivot < array[i]:
            greater_sublist.append(array[i])           
    return quick_sort(lesser_sublist) + equal_sublist + quick_sort(greater_sublist)

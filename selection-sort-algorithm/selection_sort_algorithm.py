def selection_sort(array):
    n = len(array)
    for index in range(n):
        min_index = index
        for i in range(index+1,n):
            if array[min_index] > array[i]:
                min_index = i
        if min_index != index:
            array[index], array[min_index] = array[min_index], array[index]
    return array

# eg. of usage
array = [33, 5, 89, 2, 67, 245]
print(selection_sort(array))

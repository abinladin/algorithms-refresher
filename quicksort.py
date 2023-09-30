def quicksort(array: list):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left_partition = [i for i in array[1:] if i  <= pivot]
        right_partition = [i for i in array[1:] if i > pivot]
        return quicksort(left_partition) + [pivot] + quicksort(right_partition)
    
print(quicksort([1, 4, 3, 2]))
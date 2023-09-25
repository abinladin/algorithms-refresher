def iterative_binary_search(left, right):
    iteration = 0
    while right >= left:
        iteration += 1
        middle = (right + left) // 2
        print(f"i:{iteration}: left: {left}\t middle: {middle}\t right: {right}")
        if sorted_list[middle] > search_term:
            right = middle -1
        elif sorted_list[middle] < search_term:
            left = middle + 1
        else:
            print("located " + str(sorted_list[middle]) + " on iteration " +str(iteration))
            return
        
    print(f"item {search_term} not in list")

def recursive_binary_search(left, middle, right, iteration):
    iteration += 1
    print(f"r:{iteration}: left: {left}\t middle: {middle}\t right: {right}")
    if left == right:
        print(f"term {search_term} not in list")
        return
    elif sorted_list[middle] > search_term:
        recursive_binary_search(left, (left + middle) // 2, middle - 1, iteration)
    elif sorted_list[middle] < search_term:
        recursive_binary_search(middle + 1, (middle + right) // 2, right, iteration)
    else:
        print(f"located {sorted_list[middle]} on iteration {iteration}")
        return



if __name__ == "__main__":
    sorted_list = [x for x in range(50)]
    left = 0
    right = len(sorted_list) - 1

    search_term = int(input("Input a number for me to guess!: "))
    print("iterative binary search:")
    iterative_binary_search(left, right)
    print()
    print("Recursive binary search")

    recursive_binary_search(left, (left + right) // 2, right, 0)
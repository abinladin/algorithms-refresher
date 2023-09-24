sorted_list = [x + 1 for x in range(100)]
left = 0
right = len(sorted_list) - 1

search_term = int(input("Input a number for me to guess!"))

iteration = 0
while right >= left:
    iteration += 1
    middle = (right + left) // 2
    print(f"{iteration}: left: {left}\tright: {right}\t middle: {middle}")
    if sorted_list[middle] > search_term:
        right = middle - 1
    elif sorted_list[middle] < search_term:
        left = middle + 1
    elif sorted_list[middle] == search_term:
        print("located " + str(sorted_list[middle]) + " on iteration " +str(iteration))
        break
    else:
        print("term not found")
        break

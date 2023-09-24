import random
import logging


logging.propagate = False

logging.basicConfig(level = logging.INFO)

unsorted_list = [random.randint(1, 20) for x in range(10)]

def selection_sort():
    i  = 0
    while i < len(unsorted_list):
        j = i
        largest_number_index = j
        while j < len(unsorted_list):
            if unsorted_list[j] > unsorted_list[largest_number_index]:
                largest_number_index = j
            logging.debug( f" i={i}\tj={j}\tlargestnumindex={largest_number_index}")
            logging.debug(f"list: {str(unsorted_list)}")
            j += 1

        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[largest_number_index]
        unsorted_list[largest_number_index] = temp

        i += 1


logging.info(" unsorted list: " + str(unsorted_list))
selection_sort()
logging.info(" sorted list: " + str(unsorted_list))

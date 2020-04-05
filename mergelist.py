def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None]* merged_list_size
    [index, index_my_list, index_alices_list] = [0,0,0]
    
    while( index < merged_list_size):
        is_exhausted_my_list = index_my_list >= len(my_list)
        is_exhausted_alices_list = index_alices_list >= len(alices_list)
        
        if( not is_exhausted_alices_list and 
            ( is_exhausted_my_list or alices_list[index_alices_list] < my_list[index_my_list])):
            merged_list[index] = alices_list[index_alices_list]
            index_alices_list += 1
        else: 
            merged_list[index] = my_list[index_my_list]
            index_my_list += 1
        index += 1

    return merged_list

actual = merge_lists([2, 4, 6], [1, 3, 7])
print(actual)
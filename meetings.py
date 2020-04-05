def merge_ranges(meetings):

    # Merge meeting ranges
    starttimes = {};
    for i in range(0, len(meetings)):
        starttimes[meetings[i][0]] = meetings[i]
    sorted_keys = sorted(starttimes.keys())
    
    sorted_input = []
    for key in sorted_keys:
        sorted_input.append((starttimes[key][0],starttimes[key][1]))
    
    output_index = 0
    output_arr = [sorted_input[0]]
    curr_index = 1
    while(curr_index < len(sorted_input)):
        if(output_arr[output_index][1] >= sorted_input[curr_index][0]):
            output_arr[output_index] = (output_arr[output_index][0], max(output_arr[output_index][1],sorted_input[curr_index][1]))
        else:
            output_index += 1
            output_arr.append(sorted_input[curr_index])
        curr_index += 1
    return output_arr

actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print(actual)
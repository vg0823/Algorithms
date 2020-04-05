def reverse(message, left_index, right_index):
    while(left_index < right_index):
        message[left_index], message[right_index] = message[right_index], message[left_index]
        left_index += 1
        right_index -= 1
    return

def reverse_words(message):
    reverse(message, 0, len(message)-1)
    index = 0
    prev_index = 0
    while( index < len(message) ):
        if(message[index] == ' '):
            reverse(message, prev_index, index-1)
            prev_index = index+1
        index += 1
    reverse(message, prev_index, len(message)-1)
    return

message = list('thief cake')
reverse_words(message)
print(message)
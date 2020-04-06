class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word
        words = []
        word = ''
        for i in range(0,len(input_string)):
            if(input_string[i].isalpha()):
                word += input_string[i]
            if(input_string[i] == ' ' or i == (len(input_string)-1)):
                words.append(word)
                word = ''
        word_dict = {}
        for word in words:
            if(word in word_dict):
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        print(word_dict)
        self.words_to_counts = word_dict

input = "I like cake"
word_cloud = WordCloudData(input)

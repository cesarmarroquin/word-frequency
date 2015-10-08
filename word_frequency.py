import re
from collections import Counter
from operator import itemgetter
import operator

def read_clean_file(input_file):
    """this function opens a file and strips it of punctuation and whitespace"""
    with open(input_file) as file:
        normalized_string = re.sub( r'[^A-Za-z]', ' ', file.read().lower())
        return normalized_string.split()

def word_frequency(word_list):
    """this function counts word frequency of a list of words"""
    #this converts it to a dictionary however the places arent saved
    word_list = Counter(word_list)
    #this converts it back to a list and maintains the order from the previous dictionary
    word_list = sorted(word_list.items(), key=itemgetter(1))
    return word_list

def find_top_20(top_20_words):
    """
        This function takes the whole list and spits out the top 20.

        The loop takes out the last 20 words and values.
        They are initially arranged in descending order so the
        loop reads them backwards starting from the last item.

        The loop then strips out the parantheses from the tuples
        inside each list item and formats each in the required format.
    """
    for counter in range(1, 21, 1):
        word_list_string = (str(top_20_words[-counter:][0]))
        start = '('
        end = ')'
        extra_normal = re.sub( r'[^A-Za-z0-9]', ' ',word_list_string[word_list_string.find(start)+len(start):word_list_string.rfind(end)])
        print(extra_normal)
    return top_20_words

if __name__ == '__main__':
    find_top_20(word_frequency(read_clean_file("sample.txt")))

import re
from collections import Counter
from operator import itemgetter
import operator

def read_whole_file():
    with open("sample.txt") as file:
        normalized_string = re.sub( r'[^A-Za-z]', ' ', file.read().lower())
        return normalized_string.split()

def word_frequency(word_list):
    word_list = Counter(word_list)
    word_list = sorted(word_list.items(), key=itemgetter(1))
    return word_list

def find_top_20(top_20_words):
    for counter in range(1, 21, 1):
        word_list_string = (str(top_20_words[-counter:][0]))
        start = '('
        end = ')'
        extra_normal = re.sub( r'[^A-Za-z0-9]', ' ',word_list_string[word_list_string.find(start)+len(start):word_list_string.rfind(end)])
        print(extra_normal)
    return top_20_words

if __name__ == '__main__':
    find_top_20(word_frequency(read_whole_file()))

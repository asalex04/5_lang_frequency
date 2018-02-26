import sys
import re
import collections


def load_data(filepath):
   with open(filepath) as text_file:
       text = text_file.read().lower()
       return text


def get_most_frequent_words(text):
    result = re.findall(r'\w+', text)
    most_frequent_words = collections.Counter(result).most_common(10)
    return most_frequent_words


def print_words(most_frequent_words):
    print('Ten most popular words in this text:')
    counter = 1
    for i in most_frequent_words:
        print(str(counter) + '. ' + i[0])
        counter += 1


if __name__ == '__main__':

    if len(sys.argv) > 1:
        filepath = format(sys.argv[1])
    else:
        filepath = input("Put the path to the file: ")
    try:
        text = load_data(filepath)
    except (FileNotFoundError, ValueError):
        exit('Not found correct file')

    print_words(get_most_frequent_words(text))





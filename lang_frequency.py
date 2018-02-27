import sys
import re
import collections

amount_of_words = 10

def load_data(filepath):
    with open(filepath) as text_file:
        text = text_file.read().lower()
        return text


def get_most_frequent_words(text):
    all_matches = re.findall(r'\w+', text)
    most_frequent_words = collections.Counter(all_matches)
    top_ten = most_frequent_words.most_common(amount_of_words)
    return top_ten


def print_words(most_frequent_words):
    print('Ten most popular words in this text:')
    counter = 1
    for word in most_frequent_words:
        print(str(counter) + '. ' + word[0])
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





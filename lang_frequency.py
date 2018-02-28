import sys
import re
import collections


def load_data(filepath):
    with open(filepath) as text_file:
        text = text_file.read()
        return text


def get_most_frequent_words(text):
    all_matches_words = re.findall(r'\w+', text.lower())
    most_frequent_words = collections.Counter(all_matches_words)
    amount_of_words = 10
    top_ten_words = most_frequent_words.most_common(amount_of_words)
    return top_ten_words


def print_words(most_frequent_words):
    print('Ten most popular words in this text:')
    for word, count in enumerate(most_frequent_words, 1):
        print(word, count)


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





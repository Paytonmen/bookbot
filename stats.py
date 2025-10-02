def get_book_content(filepath):
    try:
        with open(filepath) as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('file not found')
    except Exception as e:
        print(f'error: {e}')

def get_word_count(file):
    string = get_book_content(file)
    words = string.split()
    num_words = len(words)
    return num_words

def get_char_count(file):
    string = get_book_content(file)
    words = string.split()
    chardict = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char not in chardict:
                chardict[char] = 1
            else:
                chardict[char] +=1
    return chardict

def sorter(chardict):
    sorteddict = dict(sorted(chardict.items(), key=lambda item: item[1], reverse=True))
    return sorteddict


file = './books/frankenstein.txt'
chardict = get_char_count(file)
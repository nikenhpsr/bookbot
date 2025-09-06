def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    stats = {}
    for char in text.lower():
        if char.isalpha():
            if char in stats:
                stats[char] += 1
            else:
                stats[char] = 1
    return stats

def sort_on(dict_item):
    return dict_item['num']

def sort_char_counts(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_dict = {'char': char, 'num': count}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list

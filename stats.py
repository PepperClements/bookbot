
def get_num_words(text):
    words = text.split()
    return len(words)

def num_characters(text):
    count_char={}
    for char in text:
        char = char.lower()
        if char in count_char:
            count_char[char] += 1
        else:
            count_char.update({char: 1})
    return count_char

def sort_on(count_char):
    return count_char["num"]

def sort_char_count(text):
    count_char = num_characters(text)
    char_count_list = []
    for char, count in count_char.items():
        char_count_list.append({"char": char, "num": count})
    char_count_list.sort(key=sort_on,  reverse=True)
    return char_count_list


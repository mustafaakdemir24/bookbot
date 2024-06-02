def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    # countOfWords = word_count(text)
    countOfWords = get_num_words(text)
    countOfChars = get_num_chars(text)
    sortedCountOfChars = sort_dictionary(countOfChars)
    print_a_report(countOfWords, sortedCountOfChars)
    # print(sortedCountOfChars)


def get_book_text(path):
    with open(path, 'r') as f:
        file_content = f.read()
        return file_content


def word_count(text):
    count = 0
    for word in text.split():
        count += 1
    return count


def get_num_words(text):
    words = text.split()
    return len(words)


def convert_to_list(dict):
    return list(dict.items())


def get_num_chars(text):
    char_count = dict()
    lowered_text = text.lower()

    for char in lowered_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


def sort_dictionary(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)


def print_a_report(number_of_words, number_of_chars):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{number_of_words} words found in the document')
    print()

    for item in number_of_chars:
        print(f'The {item[0]} character was found {item[1]} times')

    print('--- End report ---')


main()

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        chars_dictionary = chars_count(file_contents)
        print_report(file_contents, chars_dictionary)

def word_count(text):
    words = text.split()
    return len(words)

def chars_count(text):
    chars_dict = {}
    for char in text:
        char_lowercase = char.lower()
        if char_lowercase in chars_dict:
            chars_dict[char_lowercase] += 1
        else:
            chars_dict[char_lowercase] = 1
    return chars_dict

def get_char_count(chars_dict):
    char_count = []
    for char, count in chars_dict.items():
        if char.isalpha() == True:
            char_count.append({"char" : char, "count" : count})
    char_count.sort(reverse=True, key=sort_on)
    return char_count

def sort_on(dict):
    return dict["count"]

def get_char_count_list(char_count):
    char_count_list = []
    for char_dict in char_count:
        char_count_list.append(f"The '{char_dict["char"]}' character was found {char_dict["count"]} times")
    return char_count_list

def print_report(file_contents, chars_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document")
    char_counts = get_char_count(chars_count)
    formatted_lines = get_char_count_list(char_counts)
    for line in formatted_lines:
        print(line)
        
    print("--- End report ---")
 
main()
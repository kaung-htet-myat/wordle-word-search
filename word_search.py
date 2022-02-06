import re

DICT_PATH = './data/words_alpha.txt'

def main():

    while True:
        result_list = []
        input_word = input("query word: ")
        omit_letters = input("omit letters: ")
        omit_letters = omit_letters.split()

        pattern = input_word.replace('_', '.')

        with open(DICT_PATH, 'r', encoding='utf-8') as rfile:
            for dict_word in rfile:
                cond = True
                dict_word = dict_word.strip('\n')

                if not len(dict_word) == len(input_word):
                    continue

                queried_word = re.findall(pattern, dict_word, re.IGNORECASE)
                if queried_word:
                    for letter in omit_letters:
                        cond = cond and letter.lower() not in queried_word[0]
                    if cond:
                        result_list.append(queried_word[0])

        if not result_list:
            print("no word matched")
            continue
        print(*result_list, sep='\n')


if __name__ == '__main__':
    main()
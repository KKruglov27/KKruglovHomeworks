import string
from colorama import Fore, Style

class WordsFinder:
    file_names = []

    def __init__(self, *file):
        self.file = file
        for name in file:
            self.file_names.append(name)

    def get_all_words(self):
        string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~—’'
        self.all_dicts = {}
        for file_ in self.file_names:
            with open(file_, encoding='utf-8') as words:
                words = words.read()
                words = (' '.join(word.strip(string.punctuation) for word in words.split()))
                words = [f'{line.lower()}' for line in words.split()]
                self.all_dicts.update({f'{file_}': words})
        for name, words_list in self.all_dicts.items():
             print()
             print(f"{Fore.GREEN}{name}{Style.RESET_ALL}:")
             if len(words_list) < 20:
                print(words_list)
             else:
                for x in zip(*[words_list[i::20] for i in range(20)]):
                  print(x)
        print()
      # return f"All_dicts_with_words", self.all_dicts

    def find(self, word):
        self.word_index = {}
        self.word_indexes = {}
        for name, words_list in self.all_dicts.items():
            self.all_indexes = [i + 1 for i, x in enumerate(words_list) if x == word.lower()]
            if self.all_indexes == []:
                self.all_indexes = []
                self.all_indexes.append('not found')
            self.word_index.update({name: self.all_indexes[0]})
            self.word_indexes.update({name:  self.all_indexes})
            continue
        print(f"Word's index '{Fore.BLUE}{word.upper()}{Style.RESET_ALL}' in file:", self.word_index)
        print(f"All_indexes '{Fore.BLUE}{word.upper()}{Style.RESET_ALL}' in file:", self.word_indexes)

    def count(self, word):
        self.word_count = {}
        for name, words_list in self.all_dicts.items():
            count_word = 0
            for i in words_list:
                if word == i:
                    count_word += 1
            if count_word == 0:
                count_word = 'not found'
            self.word_count.update({name: count_word})
            continue
        print(f"Words count '{Fore.BLUE}{word.upper()}{Style.RESET_ALL}' in file: ", self.word_count)
        print()


finder = WordsFinder('test_file.txt', 'Rudyard Kipling - If.txt',
                     'Mother Goose - Monday’s Child.txt', )

(finder.get_all_words())
(finder.find("text"))
(finder.count('text'))
(finder.find("is"))
(finder.count('is'))

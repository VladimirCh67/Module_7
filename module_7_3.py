from pprint import pprint
import os.path
import io

class WordsFinder:
    def __init__(self, *f_names):
        self.file_names = f_names

    def get_all_words(self):
        all_words = {}
        for i in range(len(self.file_names)):
            words_ = []
            with open(self.file_names[i], 'r', encoding = 'utf-8') as file:
                for line in file:
                    ln = line.lower() #
                    for j in [',', '.', '=', '!', '?', ';', ':', ' - ','\n']:
                        ln =ln.replace(j, ' ')
                    words_.extend(ln.split())
                all_words[self.file_names[i]] = words_

        return all_words


    def find(self, word):
        self.word = word
        f_word = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word.lower():
                    f_word[name] = i + 1
                    break

        return f_word


    def count(self, word):
        self.word = word
        c_word = {}
        cnt_ = 0
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word.lower():
                    cnt_ += 1
            c_word[name] = cnt_
        return c_word



finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')

print(finder2.get_all_words())
print(finder2.find('captain'))
print(finder2.count('captain'))


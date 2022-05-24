import re
from itertools import combinations, chain

def powerset(iterable):
    "Преобразование powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    c = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return [item for item in c if len(item)>1]


class Dictionary:
    #Класс определения словаря слов из которых будет выбрано наиболее подходящее
    #Алгоритм подбора содержится в функции find_most_similar
    def __init__(self,words):
        self.words=words

    def find_most_similar(self, term):
        changes = 100
        closest_word = ''

        count = 0
        for word in self.words:
            if len(self.words)>len(term):
                longer = word
                shorter = term
            else:
                longer = term
                shorter = word
            letters_in_selected_word = [letter for letter in shorter if letter in longer]

            for s in powerset(letters_in_selected_word):
                regex = ''
                for let in s:
                    regex += r'[A-Za-z]*' + re.escape(let)
                regex+=r'[A-Za-z]*'
                if re.search(regex, longer) and (len(longer) - len(s))<changes:
                    changes = len(longer) - len(s)
                    closest_word = word
        return closest_word

fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry']);
closest_word = fruits.find_most_similar('pineple')
print(closest_word)
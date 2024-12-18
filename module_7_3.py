

class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames

    def get_all_words(self):
        """Подготовительный метод, возвращающий словарь с файлами и словами."""
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', '-']

        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for punc in punctuation:
                    content = content.replace(punc, '')
                words = content.split()
                all_words[filename] = words

        return all_words

    def find(self, word):
        """Метод поиска первого вхождения слова в каждом файле."""
        result = {}
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            if word in words:
                index = words.index(word)
                result[filename] = index

        return result

    def count(self, word):
        """Метод подсчета количества вхождений слова в каждом файле."""
        result = {}
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            count_word = words.count(word)
            if count_word > 0:
                result[filename] = count_word

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
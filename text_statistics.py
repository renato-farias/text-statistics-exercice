from collections import namedtuple

LogestWord = namedtuple("LogestWord", "word, len")

class TextStatistics:

    def __init__(self, text_input):
        self.text_input = text_input

    @property
    def words(self):
        return TextStatistics.get_words(self.text_input)

    @property
    def num_of_words(self):
        return len(self.words)

    @property
    def sentences(self):
        return [s for s in self.text_input.split(".") if s != ""]

    @property
    def num_of_sentences(self):
        return len(self.sentences)

    @property
    def longest_word(self):
        _longest_word = max(self.words, key=len)
        return LogestWord(word=_longest_word, len=len(_longest_word))

    @property
    def unique_words(self):
        return list(set(self.words))

    @property
    def num_of_unique_words(self):
        return len(self.unique_words)

    @property
    def repeated_words(self):
        return {
            uw: self.words.count(uw)
            for uw in set(self.unique_words) if self.words.count(uw) > 1
        }

    @property
    def num_of_repeated_words(self):
        return len(self.repeated_words.keys())

    def top_repeated_words(self, top_of):
        return sorted(
            self.repeated_words.items(),
            key=lambda item: item[1],
            reverse=True)[0:top_of]

    @property
    def only_once_percentage(self):
        return round((self.num_of_unique_words / self.num_of_words ) * 100, 2)

    @property
    def average_of_words_per_sentence(self):
        words_in_sentence = []
        for sentence in self.sentences:
            words_in_sentence.append(len(TextStatistics.get_words(sentence)))
        return round(sum(words_in_sentence) / len(words_in_sentence), 2)

    def get_x_word_sentences(self, num_of_words):
        x_word_sentences = [
            sentence for sentence in self.sentences
            if len(TextStatistics.get_words(sentence)) == num_of_words
        ]
        return x_word_sentences

    def get_top_x_word_sentences(self, num_of_words, top_of):
        return self.get_x_word_sentences(num_of_words)[0:top_of]

    @staticmethod
    def get_words(s):
        _words = s.split(" ")

        for idx, word in enumerate(_words):
            if word.endswith("."):
                _words[idx] = word.rstrip('.')
                continue
            if '.' in word:
                _words.pop(idx)
                for idx2, min_word in enumerate(word.split(".")):
                    _words.insert(idx+idx2, min_word)
        return _words

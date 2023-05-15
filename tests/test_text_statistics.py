from text_statistics import TextStatistics, LogestWord

TEXT_INPUT1 = "abc abc. abc abcedf. abc. abc anc."
TEXT_INPUT2 = "abc abc. abc abccde. abc. cdf.abc anc."

def test_num_of_words():
    assert TextStatistics(TEXT_INPUT1).num_of_words == 7
    assert TextStatistics(TEXT_INPUT2).num_of_words == 8

def test_num_of_sentences():
    assert TextStatistics(TEXT_INPUT1).num_of_sentences == 4
    assert TextStatistics(TEXT_INPUT2).num_of_sentences == 5

def test_logest_word():
    assert TextStatistics(TEXT_INPUT1).longest_word == LogestWord(word="abcedf", len=6)
    assert TextStatistics(TEXT_INPUT2).longest_word == LogestWord("abccde", len=6)

def test_num_of_unique_words():
    assert TextStatistics(TEXT_INPUT1).num_of_unique_words == 3
    assert TextStatistics(TEXT_INPUT2).num_of_unique_words == 4

def test_num_of_repeated_words():
    assert TextStatistics(TEXT_INPUT1).num_of_repeated_words == 1
    assert TextStatistics(TEXT_INPUT2).num_of_repeated_words == 1

def test_top_repeated():
    assert TextStatistics(TEXT_INPUT1).top_repeated_words(top_of=1) == [("abc", 5)]
    assert TextStatistics(TEXT_INPUT2).top_repeated_words(top_of=1) == [("abc", 5)]

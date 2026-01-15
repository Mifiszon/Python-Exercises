import re

def count_words(text):
    words = re.findall(r"\w+", text)
    return len(words)

def avg_word_length(text):
    words = re.findall(r"\w+", text)
    if not words:
        return 0
    lengths = [len(w) for w in words]
    return sum(lengths) / len(lengths)

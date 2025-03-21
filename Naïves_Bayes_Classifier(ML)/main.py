from collections import Counter
from fraction import Fraction
from nltk.tokenize import regexp_tokenize, word_tokenize

import pandas as pd


def compute_likelihood(lang_corpus_freq, token, vocab_unique_word_num):
    """
    We compute the likelihood of the token given the langauge. We also apply Laplace smoothing
    to avoid having 0 as probability. A probability of 0 => a prior posteriori probability of 0
    :param lang_corpus_freq: the dict containing the frequencies of tokens of the language
    :param token: the token to compute the likelihood
    :param vocab_unique_word_num: the number of unique words in the vocabulary
    :return: the likelihood of the token given the langauge as a fraction
    """
    n = lang_corpus_freq.get(token, 0)
    n = n + 1
    return Fraction(n, sum(lang_corpus_freq.values()) + vocab_unique_word_num)

en_corpus = "Hakuna Matata! What a wonderful phrase!\nHakuna Matata!".lower()
no_corpus = "Hakkuna Matata, to besnerende ord.\nHakkuna Matata!".lower()
fr_corpus = "Hakuna matata, mais quelle phrase magnifique!\nHakuna matata!".lower()

en_word_freq = Counter(regexp_tokenize(en_corpus, "[A-z]+"))
no_word_freq = Counter(regexp_tokenize(no_corpus, "[A-z]+"))
fr_word_freq = Counter(regexp_tokenize(fr_corpus, "[A-z]+"))

lang_to_freq = {
    "English": en_word_freq,
    "French": fr_word_freq,
    "Norwegian": no_word_freq
}

# Here we create the vocabulary - the list of all the words in our corpus
vocab = set()
vocab.update(list(en_word_freq.keys()))
vocab.update(list(no_word_freq.keys()))
vocab.update(list(fr_word_freq.keys()))
vocab = list(vocab)

# The three language we are using
headers = ["English", "Norwegian", "French"]

data = []
for i in range(len(vocab)):
    data.append([0, 0, 0])
for i, word_freq in enumerate([en_word_freq, no_word_freq, fr_word_freq]):
    for word, freq in word_freq.items():
        pos = vocab.index(word)
        data[pos][i] = freq

# We create a pandas Dataframe because it is more convenient to visualise
df = pd.DataFrame(data, index=vocab, columns=headers)
print("We display the frequency per word for each language.")
print(df) # OK


# Here we are in the prediction part
# The test set
lang_to_determine = [
    "to wonderful phrase",
    "Hakuna Matata.",
    "Magnifique matata!",
    "Matata Hakkuna Matata"
]

unique_word_num = len(vocab)

result = []
for i, sent in enumerate(lang_to_determine):
    result.append([])
    probs = []
    max_prob = 0
    tokens = regexp_tokenize(lang_to_determine[i], "[A-z]+")
    for lang in headers:
        prob = 1
        for token in tokens:
            prob *= compute_likelihood(lang_to_freq[lang], token.lower(), unique_word_num)
        probs.append(prob)
        if prob > max_prob:
            max_prob = prob
    for j, prob in enumerate(probs):
        if prob == max_prob:
            result[-1].append(headers[j])
    result[-1].append(max_prob)

print("\n ###### Results: ###### \n")
for r in result:
    print(r)
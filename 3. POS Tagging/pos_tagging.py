from nltk import pos_tag
from nltk import word_tokenize, sent_tokenize

# sample_text = "I was walking by the road when I saw the cutest puppy on the other side"
#
# tokenized_words = word_tokenize(sample_text)
# tag = pos_tag(tokenized_words)
# print(tag)

with open("2001aspaceodyssey.txt", "r") as corpora:
    sample_text = corpora.read()

# print(sample_text)

tokenized_sentences = sent_tokenize(sample_text)
for sentence in tokenized_sentences:
    tokenized_words = word_tokenize(sentence)
    tag = pos_tag(tokenized_words)
    print(tag)


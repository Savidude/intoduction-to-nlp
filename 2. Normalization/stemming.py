from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# sample_words = ["legal", "illegal", "legalize", "legally"]
# for word in sample_words:
#     print(ps.stem(word))

sample_text = "It is illegal to take a U-turn in the middle of the highway. If you do, the police will take legal " \
              "action against the driver. Make sure to follow the road rules legally when driving"

tokenized_words = word_tokenize(sample_text)
for word in tokenized_words:
    print(ps.stem(word))


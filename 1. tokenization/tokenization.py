from nltk.tokenize import sent_tokenize, word_tokenize

sample_text = "Hello there Mr. Brown, how are you? The weather is nice today. How is your monther-in-law doing?"

print("Tokenized sentences:")
tokenized_sentences = sent_tokenize(sample_text)
for sentence in tokenized_sentences:
    print(sentence)

print("Tokenized words:")
tokenzed_words = word_tokenize(sample_text)
for word in tokenzed_words:
    print(word)

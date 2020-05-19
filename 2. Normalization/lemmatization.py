from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("puppies"))
print(lemmatizer.lemmatize("wolves"))
print(lemmatizer.lemmatize("churches"))
print(lemmatizer.lemmatize("abaci"))
print(lemmatizer.lemmatize("people"))

print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))

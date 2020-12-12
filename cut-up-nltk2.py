import random
import nltk
nltk.download()
from nltk import word_tokenize, sent_tokenize
from random import sample

text = """ La capacidad de escuchar es un don y crece a medida que crecemos espiritualmente. La vida adquiere un nuevo significado cuando nos abrimos a ese don
  """

words = nltk.word_tokenize(text)

print(words)
tamano=len(words)

print(tamano)
wordscambi=(sample(words, k=tamano))

for i in range(len(wordscambi)):
    print(wordscambi[i], end=" ")



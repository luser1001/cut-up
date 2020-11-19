import random
import nltk
nltk.download()
from nltk import word_tokenize, sent_tokenize
from random import sample

text = """ Un analista de seguridad con sede en España demostró nuevas trampas de captura de satélites 
que podrían permitir navegar de forma anónima con Internet de alta velocidad """
words = nltk.word_tokenize(text)

print(words)
tamano=len(words)

print(tamano)
print (sample(words, k=tamano))

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
text = "I am Krishna Bhunia, a Senior Software Engineer and Data Scientist and Engineer with expertise on machine learning and NLP"

tokenized_text = nltk.tokenize.sent_tokenize(text)
print(f"Tokenized text {tokenized_text}")

for n in tokenized_text:
    wordsList = nltk.word_tokenize(n)

print(f"wordlist {wordsList}")
wordsList_NSP = [w for w in wordsList if not w in stop_words]
print(f"Non Stop Words {wordsList_NSP}")

stopWordsList = [w for w in wordsList if w in stop_words]
print(stopWordsList)

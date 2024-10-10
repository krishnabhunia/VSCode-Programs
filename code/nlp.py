import spacy

print("\nSimilarity Starts")
# Load the pre-trained model with word vectors
nlp = spacy.load("en_core_web_md")

# Input words
word1 = nlp("i love football")
word2 = nlp("you hate cricket")

# Compute similarity using the `similarity` method
similarity_score = word1.similarity(word2)

print(f"Similarity between '{word1}' and '{word2}': {similarity_score}")
print("Similarity Ends")

print("\nTokenization Starts")
text = "The head office of Google is in California"
document = nlp(text)
for ent in document.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
print("Tokenization Ends")

print("\nTokenization Starts")
text = "I am Krishna Bhunia, a Senior Software Engineer and Data Scientist and Engineer with expertise on machine learning and NLP"
document = nlp(text)
for ent in document.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
print("Tokenization Ends")
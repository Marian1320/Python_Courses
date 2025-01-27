# Write a function that counts the number of words in a sentence.
def count_words(sentence):
    word=sentence.split()
    return len(word)
print(count_words('hello world'))
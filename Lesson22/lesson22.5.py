# Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.

def words_lengths(words):
    word_length = {word: len(word) for word in words if len(word) > 3}
    return word_length

word_list = ["apple", "cat", "table", "dog"]
result = words_lengths(word_list)
print(f"words with lengths > 3: {result}")

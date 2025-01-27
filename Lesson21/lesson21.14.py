# Write a function that capitalizes the first letter of each word in a sentence.

def capitalize_words(sentence):
    return ' '.join([word.capitalize() for word in sentence.split()])

print(capitalize_words("hello world"))

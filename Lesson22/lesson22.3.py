# Create a list of vowels present in a given word.
def find_vowels(word):
    vowels = "aeiouAEIOU"
    return [char for char in word if char in vowels]


word = "Mariana"
result = find_vowels(word)
print(f"Vowels are {result}")

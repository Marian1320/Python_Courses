# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.

books = {
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Pride and Prejudice": "Jane Austen",
}

def find_author(book_title, book_dict):
    if book_title in book_dict:
        return book_dict[book_title]
    else:
        return "Book not found"

book_title = "The Great Gatsby"
author = find_author(book_title, books)
print(f"The author of '{book_title}' is {author}")


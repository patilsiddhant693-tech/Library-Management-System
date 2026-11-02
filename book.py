class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_details(self):
        print("Book ID:", self.book_id)
        print("Book Title:", self.title)
        print("Author:", self.author)


book1 = Book(
    101,
    "Python Programming",
    "Guido van Rossum"
)

book1.display_details()

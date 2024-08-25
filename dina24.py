class Book:
    def __init__(self, title, author, pages):  # Corrected constructor method
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def compare_pages(self, other_book):
        if self.pages > other_book.pages:
            return f"{self.title} has more pages than {other_book.title}"
        elif self.pages < other_book.pages:
            return f"{self.title} has fewer pages than {other_book.title}"
        else:
            return f"{self.title} and {other_book.title} have the same number of pages"

# Create instances of the Book class
book1 = Book("Book A", "Author A", 200)
book2 = Book("Book B", "Author B", 250)

# Display information about the books
book1.display_info()
book2.display_info()

# Compare the number of pages
print(book1.compare_pages(book2))

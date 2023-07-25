class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.checked_out = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"

    def checkout(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available in the library.")


class Book(LibraryItem):
    def __init__(self, title, author, publication_year, isbn):
        super().__init__(title, author, publication_year)
        self.isbn = isbn

    def __str__(self):
        return f"Book - {super().__str__()}, ISBN: {self.isbn}"


class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, issue_number):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number

    def __str__(self):
        return f"Magazine - {super().__str__()}, Issue Number: {self.issue_number}"


# Test the classes
if __name__ == "__main__":
    # Create instances of Book and Magazine
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951, "978-0-316-76948-4")
    magazine1 = Magazine("National Geographic", "National Geographic Society", 1888, "July 2023")

    # Checkout and return items
    book1.checkout()
    book1.return_item()
    book1.checkout()

    magazine1.checkout()
    magazine1.return_item()

    # Print information about each library item
    print(book1)
    print(magazine1)

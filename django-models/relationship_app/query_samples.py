# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    author_name = "Author Name"  # replace with the actual author's name
    books_by_author = Book.objects.filter(author__name=author_name)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(book.title)

    # List all books in a library
    library_name = "Library Name"  # replace with the actual library's name
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(book.title)

    # Retrieve the librarian for a library
    librarian = library.librarian
    print(f"Librarian of {library_name}: {librarian.name}")

if __name__ == "__main__":
    run_queries()

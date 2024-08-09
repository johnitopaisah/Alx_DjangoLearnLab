from bookshelf.models import Book


# Delete Operation

```python
# Deleting the Book instance
book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Verifying deletion
Book.objects.all()
# Output: <QuerySet []>

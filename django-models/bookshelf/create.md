# Create Operation

```python
# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
# Output: <Book: 1984>

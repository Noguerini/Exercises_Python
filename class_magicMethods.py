class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return self.num_pages < other.num_pages


book1 = Book("The Hobby", "GRR Tolkien", 310)
book2 = Book("HATPS", "JK Rowling", 223)
book3 = Book("Narnia", "idk", 300)


print(book1)

print(book1 == book2)
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"

def main():
    # Sample usage
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    publication_year = input("Enter the publication year: ")
    
    # Validate the publication year
    try:
        publication_year = int(publication_year)
        book = Book(title, author, publication_year)
        print(book)
    except ValueError:
        print("Please enter a valid integer for the publication year.")

if __name__ == "__main__":
    main()

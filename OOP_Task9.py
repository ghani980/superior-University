import csv


class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        
        super().__init__(title, author)
        if genre and pages:
            self.genre = genre
            self.pages = pages
        else:
            self.genre = "Unknown"
            self.pages = 0
    
    def display_info(self):
      
        super().display_info()  
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")
    
   
    def set_book_info(self, title, author, genre=None, pages=None):
        self.title = title
        self.author = author
        if genre and pages:
            self.genre = genre
            self.pages = pages
        else:
            self.genre = "Unknown"
            self.pages = 0


class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
      
        super().__init__(title, author)
        if journal and doi:
            self.journal = journal
            self.doi = doi
        else:
            self.journal = "Unknown"
            self.doi = "Unknown"
    
    def display_info(self):
       
        super().display_info()  
        print(f"Journal: {self.journal}")
        print(f"DOI: {self.doi}")
    
    
    def set_article_info(self, title, author, journal=None, doi=None):
        self.title = title
        self.author = author
        if journal and doi:
            self.journal = journal
            self.doi = doi
        else:
            self.journal = "Unknown"
            self.doi = "Unknown"


def save_documents_to_file(filename, documents):
    """Saves all documents (Books and Articles) to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Title', 'Author', 'Genre/Journal', 'Pages/DOI'])
        for doc in documents:
            if isinstance(doc, Book):
                writer.writerow(['Book', doc.title, doc.author, doc.genre, doc.pages])
            elif isinstance(doc, Article):
                writer.writerow(['Article', doc.title, doc.author, doc.journal, doc.doi])

def read_documents_from_file(filename):
    """Reads documents from a CSV file and returns a list of Document objects."""
    documents = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                doc_type, title, author, extra_info1, extra_info2 = row
                if doc_type == 'Book':
                    documents.append(Book(title, author, extra_info1, int(extra_info2)))
                elif doc_type == 'Article':
                    documents.append(Article(title, author, extra_info1, extra_info2))
    except FileNotFoundError:
        print(f"{filename} not found. A new file will be created.")
    return documents


if __name__ == "__main__":
    
    filename = 'documents.csv'

    
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 218)
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    article1 = Article("Quantum Computing", "John Doe", "Science Journal", "10.1234/qcomp.2024")

    
    documents = [book1, book2, article1]

    
    save_documents_to_file(filename, documents)

    
    print("\nDocuments Loaded from File:")
    loaded_documents = read_documents_from_file(filename)
    for doc in loaded_documents:
        doc.display_info()
        print()


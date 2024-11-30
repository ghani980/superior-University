
class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Book(Item):
    def __init__(self, title, author, pages):
        super().__init__(title, author)  
        self.pages = pages
    
    def additional_info(self):
        
        print(f"Pages: {self.pages}")


class Magazine(Item):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)  
        self.issue_number = issue_number
    
    def additional_info(self):
        # Method to display additional info about the magazine
        print(f"Issue Number: {self.issue_number}")

if __name__ == "__main__":
    book = Book("Python Programming", "John Doe", 350)
    print("Book Info:")
    book.display_info()
    book.additional_info()
    print()


    magazine = Magazine("Tech Monthly", "Jane Smith", 42)
    print("Magazine Info:")
    magazine.display_info()
    magazine.additional_info()

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def show_info(self):
        print(f"title of book{self.title}, and the author is {self.author}")


book1 = Book("harry potter","gitler")
book1.show_info()
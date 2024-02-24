class LibraryManagementSystem:
    #constructor
    def __init__(self):
        self.books = []

    def adding_books(self,title,author,copies):
        book = {
            "title":title,
            "author":author,
            "copies":copies,
            "available_copies":copies
        }
        self.books.append(book)
        print(f"{title} book has been added successfully!")
    
    #displaying the books
    def display_books(self):
        if self.books:
            print("Books Details:")
            for book in self.books:
                print(f"The Book Title: {book['title']} | Author: {book['author']} | Available Books: {book['available_copies']}")
        else:
            print("No books avaialable in library")

    #helper function
    def find_book(self,title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None
    #barrow books
    def barrow_book(self,title):
        book = self.find_book(title)
        if book is not None:
            if book['available_copies'] <= book['copies']:
                book['available_copies'] -= 1# i -= 1 => i = i-1
                print(f"{title} book has been barrowed successfully!")
        else:
            print(f"{title} book is not available in library!")
    
    #return books
    def return_book(self,title):
        book = self.find_book(title)
        if book is not None:
            if book['available_copies'] <= book['copies']:
                book['available_copies'] += 1
                print(f"{title} book has retured succesfully!")
        else:
            print(f"{title} book not belongs to library")


        

    


s = LibraryManagementSystem()
# s.adding_books("Algorithm","alen",5)
# s.adding_books("Pythonbook","bob",10)
# # s.display_books()
# s.barrow_book('Algorithm')
# s.barrow_book('Algorithm')
# s.barrow_book('Algorithm')
# s.display_books()
# s.return_book('Algorithm')
# s.display_books()

while True:
    n = int(input("Enter 1:Adding book | 2.Display book | 3.Barrow book | 4.Return book | 5.Quit"))
    if n == 1:
        title = input("Enter the name of book which you need to add")
        author = input("Enter the author name")
        copies = int(input("Enter the number of copies"))
        s.adding_books(title,author,copies)
    elif n==2:
        s.display_books()
    elif n==3:
        title = input("Enter the title of the book to barrow")
        s.barrow_book(title)
    elif n==4:
        title = input("Enter the title of the book to return")
        s.return_book(title)
    else:
        quit()
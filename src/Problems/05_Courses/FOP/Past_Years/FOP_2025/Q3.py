# Library Class
class LibraryMaterial:
    title: str
    author: str
    borrowed: bool
    due_date: int

    def __init__ (self, title: str, author: str, borrowed: bool = False, due_date: int = 0):
        self.title = title
        self.author = author
        self.borrowed = borrowed
        self.due_date = due_date
    
    def borrow (self):
        if (self.borrowed):
            print('The item "{0}" by "{1}" is currently unavailable and should be available by [Today\'s Date + {2}days]'.format(self.title, self.author, self.due_date))
            print()
            return
        
        self.borrowed = True
        self.due_date = 14
        print("Material borrowed successfully.")
        print("Due date for return: [Today's Date + %ddays]" % self.due_date)
        print('The item "{0}" by "{1}" is successfully borrowed and should be returned after [Today\'s Date + {2}days]'.format(self.title, self.author, self.due_date))
        print()

# DVD Class
class DVD(LibraryMaterial):
    def __init__ (self, title: str, author: str, borrowed: bool = False, due_date: int = 0):
        super().__init__(title, author, borrowed, due_date)
    
    def borrow (self):
        if (self.borrowed):
            print('The item "{0}" by "{1}" is currently unavailable and should be available by [Today\'s Date + {2}days]'.format(self.title, self.author, self.due_date))
            print()
            return 

        self.borrowed = True
        self.due_date = 5 
        print("DVD borrowed successfully.")
        print("Due date for return: [Today's Date + %ddays]" % self.due_date)
        print('The item "{0}" by "{1}" is successfully borrowed and should be returned after [Today\'s Date + {2}days]'.format(self.title, self.author, self.due_date))
        print()

# Main Class
if __name__ == "__main__":
    libraryMaterial = LibraryMaterial("My book", "Saiket Das")
    libraryMaterial.borrow()
    libraryMaterial.borrow()
    
    dvd = DVD("DVD Player", "AR Shojib")
    dvd.borrow()
    dvd.borrow()

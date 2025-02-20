from abc import ABC, abstractmethod

# Question 2 (a)

# Book class
class Book:
    title: str
    author: str
    yearPublished: int

    def __init__ (self, title: str, author: str, yearPublished: int):
        self.title = title
        self.author = author
        self.yearPublished = yearPublished
    
    def __str__ (self):
        return f"'{self.title}' was written by {self.author} in {self.yearPublished}"

# Question 2 function
def Q2_a ():
    newBook = Book("My Story", "Ahan Bryan", 2024) 
    print(newBook.__str__())


Q2_a()

# ---------------------------
# Question 2 (b)
# Custom Exception or Error class
class CustomException(Exception):
    def __init__ (self, errorMessage: str = "Custom error message"):
        self.errorMessage = errorMessage
        super().__init__(self.errorMessage)


def checkAge (age: int) -> CustomException:
    if (age < 18):
        raise CustomException("You are underage to vote!")
    else:
        print("Welcome to vote")

def Q2_b ():
    try:
        checkAge(17)
    except CustomException as error:
        print(error)


Q2_b()


# ------------
class Play(ABC):
    @abstractmethod
    def play(self):
        pass

class Guitar(Play):
    def play(self):
        print("Guitar is playing")

class Piano(Play):
    def play(self):
        print("Piano is playing")


guitar = Guitar()
piano = Piano()

guitar.play()
piano.play()



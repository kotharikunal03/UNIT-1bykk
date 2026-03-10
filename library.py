class Library:
    def __init__(self, name, author, available):
        self.name = name
        self.author = author
        self.available = available

    def check_out(self):
        self.available = False

    def return_book(self):
        self.available = True

    def display(self):
        print(self.name, self.author, self.available)


b1 = Library("Python", "ABC", True)
b1.display()
class LibraryItem:
    def borrow_item(self, title, is_borrowed):
        self.title = title
        self.is_borrowed = is_borrowed
        if self.is_borrowed == True:
            raise Exception(f"The item {self.title} is already borrowed")
        else:
            self.is_borrowed = True
            print("System Update")
    def return_item(self, title, is_returned):
        self.title = title
        self.is_returned = is_returned
        if self.is_returned == True:
            raise Exception(f"The item {self.title} is already returned")
        else:
            self.is_returned = True
            print("System Update")

t1 = LibraryItem()
t1.borrow_item("Ramayana", True)
print("Hello World")

class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_in = True
        self.name = ''
        self.date = ''

    def check_out(self, who, when):
        if self.is_in:
            self.name = who
            self.date = when
            self.is_in = False
            print(self.title + ' was taken by ' + self.name + ' on ' + self.date + '.')
        else:
            print('The item is already checked out. Sorry.')

    def return_item(self, when):
        if not self.is_in:
            self.date = when
            self.is_in = True
            print(self.title + ' was returned by ' + self.name + ' on ' + self.date + '.')
            self.name = ''
        else:
            print('This item is already in library.')

    def print_details(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, nr_pages):
        super().__init__(title, author)
        self.nr_pages = nr_pages

    def print_details(self):
        print(self.title + ' is a book written by ' + self.author + '. It has ' + str(self.nr_pages) + ' number of pages.')


class DVD(LibraryItem):
    def __init__(self, title, author, time):
        super().__init__(title, author)
        self.time = time

    def print_details(self):
        print(self.title + ' is a DVD made by ' + self.author + '. It lasts ' + str(self.time) + ' hours.')


class Magazine(LibraryItem):
    def print_details(self):
        print(self.title + ' is a magazine produced by ' + self.author + '.')


book = Book('Red Blessing', 'May Tina', 1351)
dvd = DVD('Cardigan', 'Taylor Swift', 1)
mag = Magazine('The News', 'Colourful')

book.print_details()
dvd.print_details()
mag.print_details()

book.check_out('Pheonix', '14 February')
book.check_out('Black Dragon', '19 April')
book.return_item('18 October')
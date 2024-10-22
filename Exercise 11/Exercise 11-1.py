class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        Publication.__init__(self,name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(f"Book name {self.name}, author {self.author}, page count {self.page_count}")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        Publication.__init__(self,name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Magazine name {self.name}, chief editor {self.chief_editor}")

#main
publication_list = [Magazine("Donald Duck", "Aki Hyyppä"),
                    Book("Compartment No. 6", "Rosa Liksom", 192)]
publication_list[0].print_information()
publication_list[1].print_information()
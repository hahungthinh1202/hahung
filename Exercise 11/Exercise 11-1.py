class publication:
    def __init__(self,name):
        self.name = name

class book(publication):
    def __init__(self,name, author, page_count):
        publication.__init__(self,name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(f"Book name {self.name}, author {self.author}, page count {self.page_count}")

class magazine(publication):
    def __init__(self,name,chief_editor):
        publication.__init__(self,name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Magazine name {self.name}, chief editor {self.chief_editor}")

#main
publication_list = []
publication_list.append(magazine("Donald Duck","Aki Hyyppä"))
publication_list.append(book("Compartment No. 6","Rosa Liksom", 192))

publication_list[0].print_information()
publication_list[1].print_information()
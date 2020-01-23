class Squad:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.description = ''
        self.peoplenumber = 0
        self.languagebackend = ''
        self.frameworkfrontend = ''
    
    def create(self, id, name, description, peoplenumber, languagebackend, frameworkfrontend):
        self.id =  id
        self.name = name
        self.description = description
        self.peoplenumber = peoplenumber
        self.languagebackend = languagebackend
        self.frameworkfrontend = frameworkfrontend

    def __str__(self):
        return f'{self.id}|{self.name}|{self.description}|{self.peoplenumber}|{self.languagebackend}|{self.frameworkfrontend}'

squad = Squad()
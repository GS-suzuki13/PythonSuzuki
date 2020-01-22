class Squad:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.description = ''
        self.peoplenumber = 0
        self.languagebackend = ''
        self.framewokfrontend = ''

    def __str__(self):
        return f'{self.id}|{self.name}|{self.description}|{self.peoplenumber}|{self.languagebackend}|{self.framewokfrontend}'

squad = Squad()
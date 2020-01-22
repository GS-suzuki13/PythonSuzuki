class Person:
    id = 0
    name = ''
    last_name = ''
    age = 0
    address_id = 0
    
    def __str__(self):
        return f''''{self.id}
                    {self.name}
                    {self.last_name}
                    {self.age}
                    {self.address_id}''''
class Address:
    id = 0
    cep = ''
    street = ''
    number = ''
    neighborhood = ''
    city = ''

    def __str__(self):
        return f""""{self.id}
                    {self.cep}
                    {self.street}
                    {self.number}
                    {self.neighborhood}
                    {self.city}"""
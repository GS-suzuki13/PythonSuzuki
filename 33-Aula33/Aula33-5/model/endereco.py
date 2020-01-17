class Endereco:
    id = 0
    cep = ''
    rua = ''
    numero = 0
    bairro = ''
    cidade = ''

    def exportar_txt(self, lista_endereco):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('33-Aula33/Aula33-5/endereco.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for e in lista_endereco:
                arquivo.write(f"{str(p)}\n")
    
    def __str__(self):
        return f'{self.id}|{self.cep}|{self.rua}|{self.numero}|{self.bairro}|{self.cidade}'
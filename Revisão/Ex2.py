def concatenacao(str1:str, str2:str) -> str:
    concatenacao_de_str = str1 + str2
    return concatenacao_de_str


a = input("Digite primeira String: ")
b = input("Digite segunda String: ")
resultado = concatenacao(a, b)
print (f"Junção de Strings: {resultado}")

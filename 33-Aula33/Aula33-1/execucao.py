from lista_pessoas import listar_todos
from converter_tabela import converter_tabela_dicionario
from exportar_p_txt import exportar_txt

lpt = listar_todos()
lpd = converter_tabela_dicionario(lpt)
exportar_txt(lpd)
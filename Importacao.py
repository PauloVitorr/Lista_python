from Controle import Televisao
from Contador_Letras import contador_letras, teste


if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = print(contador_letras(lista))
    print('total de letras por palavra da lista: {}'.format(total_letras))
    print('teste()')
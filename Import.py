def escrever_arquivo(texto):
    diretorio = 'C:\Users\paulo\App Python'
    arquivo = open('teste.txt', 'w')
    arquivo.write('Texto')
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write('Texto')
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open('teste.txt')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('Segunda linha\n')
    ler_arquivo('teste.txt')
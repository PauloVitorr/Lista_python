Contador_Letras = lambda lista: [len(x) for x in lista]
lista_animais = ['Cachorro', 'Gato', 'Elefante']
print(Contador_Letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(5, 10))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda  a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']
print('A soma é: {}'.format(soma(10, 5)))
print('A subtração é: {}'.format(subtracao(41, 20)))
print('A multiplicação é: {}'.format(multiplicacao(2, 20)))
print('A divisão é: {}'.format(divisao(80, 4)))
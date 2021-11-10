a = int(input('Primeiro bimestre:' ))
if a > 10:
    a = int(input('Você digitou errado. Por favor, digite novamente: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Por favor, digite novamente: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Por favor, digite novamente: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Por favor, digite novamente: '))

media = (a + b + c + d ) / 4
print('media: {}'.format(media))
if media >= 6:
    print('Parabéns, você passou!!')
else:
    print('Reprovado!')
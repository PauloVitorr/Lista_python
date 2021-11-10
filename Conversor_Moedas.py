print('Converta seu real')
real = float(input('Insira quantos R$ você possui: '))
moeda = input('A qual moeda deseja converter?' )
dólar = real / 5.23
dólar_canadense = real / 4.17
euro = real / 6.16
libra = real / 7.26
peso_argentino = real / 0.54
iene = real / 0.47
if moeda == 'dólar':
    print(f'{dólar:,.2f}')
elif moeda == 'dólar_canadense':
    print(f'{dólar_canadense:,.2f}')
elif moeda == 'euro':
    print(f'{euro:,.2f}')
elif moeda == 'libra':
    print(f'{libra:,.2f}')
elif moeda == 'peso_argentino':
    print(f'{peso_argentino:,.2f}')
elif moeda == 'iene':
    print(f'{iene:,.2f}')
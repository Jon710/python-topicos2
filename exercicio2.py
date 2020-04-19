# 2. Escreva uma função que receba um ano e determine se ele é ou não bissexto. (2,5 pontos)
# As regras são as seguintes:
# i. Anos múltiplos de 4 são bissextos
# ii. Anos múltiplos de 100 não são bissextos
# iii. Anos múltiplos de 400 são bissextos
# iii) prevalece sobre ii), que prevalece sobre i)


def ano_eh_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print('SIM! {} é bissexto.'.format(ano))
    else:
        print('NÃO! {} não é bissexto.'.format(ano))


ano = int(input('Digite o ano: '))

ano_eh_bissexto(ano)
ano_eh_bissexto(1996)
ano_eh_bissexto(1997)
ano_eh_bissexto(2555)

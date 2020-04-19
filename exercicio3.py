# 3. Pesquise sobre como abrir e ler um arquivo de texto.
# Então escreva uma programa que leia cada palavra de um arquivo (cujo nome o usuário do programa irá especificar)
# e gere uma estatística com o percentual dos caracteres que são letras (minúsculas ou maiúsculas),
# algarismos ou outros símbolos. O programa deve imprimir esses percentuais num formato apropriado. (2,5 pontos)


nome_arquivo = input('Digite o nome do arquivo: ')
arquivo = open(nome_arquivo+'.txt', 'w')
conteudo = input('Digite o conteúdo do arquivo \n')
arquivo.write(conteudo)
arquivo.close()

arquivo = open(nome_arquivo+'.txt', 'r')

palavras = []
palavras_separadas = []
caracteres = []

for linha in arquivo:
    palavras.append(linha.strip())

for i in range(len(palavras)):
    palavras_separadas += palavras[i].split()


letra_minuscula = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
letra_maiuscula = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
algarismos = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'

conta_letra = 0
conta_numero = 0
conta_resto = 0
conta_total = 0

for i in range(len(palavras_separadas)):
    for j in range(len(palavras_separadas[i])):
        caracteres += palavras_separadas[i][j]
        if(palavras_separadas[i][j] in letra_minuscula):
            conta_letra += 1
            conta_total += 1
        elif(palavras_separadas[i][j] in letra_maiuscula):
            conta_letra += 1
            conta_total += 1
        elif (palavras_separadas[i][j] in algarismos):
            conta_numero += 1
            conta_total += 1
        else:
            conta_resto += 1
            conta_total += 1


def gera_estatistica(letras, numeros, simbolos, total):
    porcentagem_letras = (letras*100) / total
    porcentagem_numeros = (numeros*100) / total
    porcentagem_simbolos = (simbolos*100) / total

    print('\nDos {} caracteres do arquivo:\n{} são letras - {:.2f}%\n{} são numeros - {:.2f}%\n{} são outros símbolos - {:.2f}%\n'
          .format(total, letras, porcentagem_letras, numeros, porcentagem_numeros, simbolos, porcentagem_simbolos))


gera_estatistica(conta_letra, conta_numero, conta_resto, conta_total)


arquivo.close()

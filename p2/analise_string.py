# lista que será traduzida
list_of_words = ['thy', 'thine', 'thee', 'thou', 'hath']

# função que busca as palavras e quantidade total das palavras do Middle English
def find_middle_english_words(text):
    # lista que irá conter as palavras, entre as que estão na lista, encontradas no texto
    words_found = []
    counter = 0  # contador para armazenar o numero total de palavras do Ingles Arcaico
    text = text.split()  # separa o livro/soneto aberto em uma lista de strings
    for word in text:
        for i in range(len(list_of_words)):
            if word == list_of_words[i]:
                # adiciona cada palavra encontrada no fim da lista.
                words_found.append(word)
                counter += 1
    print('No total, há {} palavras do Inglês Arcaico (Middle English). As encontradas foram: {}.'.format(
        counter, words_found))
    translate_words(
        input('Digite a palavra que será traduzida para o português: '))

def translate_words(word):  # função que traduz as palavras da lista para o portugues
    if word == list_of_words[0]:
        print('Thy -> teu, teus')
    elif word == list_of_words[1]:
        print('Thine -> teus')
    elif word == list_of_words[2]:
        print('Thee -> ti')
    elif word == list_of_words[3]:
        print('Thou -> tu, vós')
    elif word == list_of_words[4]:
        print('Hath -> ter, tem')
    else:  # caso seja uma palavra fora da lista, imprime isso
        print('Essa palavra não está na lista!!!')


def read_book(path):  # funcão para abrir e ler o texto escolhido. 'sonetos.txt' por exemplo
    with open(path, 'r', encoding='utf8') as file:
        text = file.read()
    return text

text = read_book(input('Arquivo do livro a ser lido: '))

find_middle_english_words(text)

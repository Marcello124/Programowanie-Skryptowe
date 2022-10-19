print('Ładowanie modułu "{0}"'.format(__name__))

############################################
def zapisz(list):
    
    elements = [element for element in set(list)]
    count = [0 for _ in elements]

    for element in list:
        count[elements.index(element)] += 1

    return [[element, counter] for element, counter in zip(elements, count)]


def wypisz(list):
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    for i in range(len(list) - 1):
        print(f"{list[i][0]}:{list[i][1]}", end=',')
    print(f'{list[-1][0]}:{list[-1][1]}')


############################################
print('Załadowano moduł "{0}"'.format(__name__))

if __name__ == '__main__':
    lista = [1, 2, 2, 3, 4, 3, 1, 5, 5, 2, 3, 2]
    lista = zapisz(lista)
    print(lista)
    wypisz(lista)
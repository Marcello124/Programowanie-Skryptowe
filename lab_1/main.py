products = {'phone': 1000, 'computer': 3000, 'apple': 2, 'pen': 20}
stock = {'phone': 10, 'computer': 5, 'apple': 20, 'pen': 10}

def sell(product, quantity, ballance, client_surname):
    if quantity > stock[product]:
        return 'out of stock'

def refund(product, quantity, ballance, client_surname):
    pass

def log(transactions, stock, ballance):
    if not len(transactions):
        return f'no transactions\n{[print(f"{x}: {y}") for x in stock.keys for y in stock.values]}\nballance: {ballance}'
    return f'{transactions}\n{[print(f"{x}: {y}") for x in stock.keys for y in stock.values]}\nballance: {ballance}'

if __name__ == '__main__':
    pass
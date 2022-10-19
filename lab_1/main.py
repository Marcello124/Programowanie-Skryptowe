import string


products = {'phone': 10, 'computer': 5, 'apple': 20, 'pen': 10}
logs = []

def sell(product, quantity, client_surname):
    if product not in products.keys():
        return 'product does not exist'
    
    elif isinstance(quantity, str):
        if not quantity.isdigit():
            return 'quantity not a number'
        else:
            quantity = int(quantity)

    elif quantity > products[product]:
        return 'out of stock'
    
    elif client_surname == '':
        return 'no surname provided'
    for letter in client_surname:
        if letter in string.punctuation + string.digits:
            return 'incorrect surname'
    
    products[product] -= quantity
    logs.append(f'{client_surname} bought {quantity} {product}')

    return 'transaction_successful'

def refund(product, quantity, client_surname):
    if product not in products.keys():
        return 'product does not exist'
    
    elif isinstance(quantity, str):
        if not quantity.isdigit():
            return 'quantity not a number'
        else:
            quantity = int(quantity)

    elif quantity > products[product]:
        return 'out of stock'
    
    elif client_surname == '':
        return 'no surname provided'
    for letter in client_surname:
        if letter in string.punctuation + string.digits:
            return 'incorrect surname'

    products[product] += quantity
    logs.append(f'{client_surname} refund {quantity} {product}')

    return 'transaction_successful'


def log(transactions, stock):
    if not len(transactions):
        return f'no transactions\n{[print(f"{x}: {stock[x]}") for x in stock.keys()]}'
    return f'{transactions}\n{[print(f"{x}: {stock[x]}") for x in stock.keys()]}'

if __name__ == '__main__':
    while True:
        transaction = input()
        if not transaction.isprintable():
            exit()
        
        if transaction[0] == 'sell':
            sell(transaction[1], transaction[2], transaction[3])
        elif transaction[1] == 'refund':
            refund(transaction[1], transaction[2], transaction[3])
        print(logs)

        # except(EOFError):
        log(logs, products)

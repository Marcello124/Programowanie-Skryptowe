# from sys import argv
# import itertools as iter


# files = argv[1:]
# numbers = []
# for file in files:
#     with open(file, 'r') as file:
#         for line in file.readlines():
#             for number in line.rstrip().split():
#                 if not int(number) % 2:
#                     numbers.append(number)
# print(len(numbers))

# numbers = [int(number) for file in files for line in open(file, 'r').readlines() for number in line.rstrip().split()]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(len(result))

from sys import argv; result = len(list(filter(lambda x: x % 2 == 0, [int(number) for file in argv[1:] for line in open(file, 'r').readlines() for number in line.rstrip().split()]))); print(result)

# # lista tylko z parzystymi liczbami w zakresie od 0 do 13
# [num for num in range(14)]
# # lista kombinacji z powtórzeniami liczb z zakresu 3 : [(0, 0), (0, 1), ... (2, 1), (2, 2)]
# [(x, y) for x in range(3) for y in range(3)]
# list(iter.product(range(3), range(3)))
# list(iter.product(range(3), repeat=2))
# # lista z liczbami z zakresu 5 w postaci: [(0, 0), (1, 1),...]
# [(x, y) for x, y in zip(range(3), range(3))]
# # lista z co drugim znakiem ze stringa 'Ada słodziak :3'
# ''.join(list(iter.compress('Ada slodziak :3', iter.cycle([0, 1]))))
# # 3 pierwsze nie wymagają żadnych bilbiotek

# # python -c "import itertools as iter; ''.join(list(iter.compress(iter.count(), iter.cycle([0, 1]))))"
# # python3 -c "import itertools as iter; ''.join(list(iter.chain(iter.pairwise(iter.compress(iter.count(), iter.cycle([0, 1]))))))"

# names = ['julka', 'bartek', 'kisiel']


# letters = []
# for name in names:
#     for letter in name:
#         letters.append(letter)


# letters = [letter for name in names for letter in name]
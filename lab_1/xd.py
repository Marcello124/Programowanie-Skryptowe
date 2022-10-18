with open("parzystość.py", "a") as file:
    file.write("number = 50\n\n")
    for i in range(10000000):
        if not i % 2:
            file.write(f'if number == {i}:\n\tprint("Parzysta")\n')
        else:
            file.write(f'elif number == {i}:\n\tprint("Nieparzysta")\n')

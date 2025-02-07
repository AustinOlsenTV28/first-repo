textToPrint = input('''What do you want to print?
''').split()

print('* * * * * * * * *')
for word in textToPrint:
    spaces = ' '
    if len(word) <= 10:
        spacesForLastStar = (14 - len(word) - 1)
        for i in range(spacesForLastStar):
            spaces += ' '
    print('*', word + spaces + '*')
print('* * * * * * * * *')
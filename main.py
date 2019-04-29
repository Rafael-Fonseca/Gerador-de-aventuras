from modelCharacter import Character

stop = False
while stop is False:
    char = Character()
    print(char)
    print()

    control = input('Deseja continuar (s/n)? ').lower()
    while control not in 'sn' and control != 'sn':
        control = input('Deseja continuar (s/n)? ').lower()

    if control == 'n':
        stop = True

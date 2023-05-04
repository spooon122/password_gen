import random as r


def chars(characters):
    for c in range(65, 91):
        characters.append(chr(c))
    return characters


def chars1(characters):
    for c in range(97, 123):
        characters.append(chr(c))
    return characters


def pass_gen(p_count, p_range, a):
    done_pass = ''
    for i in range(p_count):
        if a == '':
            print('Все условия поставлены на нет')
            break
        else:
            done_pass = r.sample(a, p_range)
            r.shuffle(done_pass)
        print(*done_pass, sep='')


characters1 = []
characters2 = []
spec_symbols = ['!', '#', '$', '%', '&', '*', '+', '-', '=', '?', '@', '^', '_']
chars1(characters2)
chars(characters1)
integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
pass_count, pass_range = int(input('Pass Count: ')), int(input('Длина: '))
first_pass = ''
is_numbers = input('Хотите иметь цифры в пароле? (Да: д//Нет : н): ')
is_upper = input('Хотите иметь ЗАГЛАВНЫЕ буквы в пароле? (Да: д//Нет : н): ')
is_lower = input('Хотите иметь строчные в пароле? (Да: д//Нет : н): ')
special_symbols = input('Хотите иметь спец.символы в пароле? (Да: д//Нет : н): ')
if 'д' in is_numbers:
    first_pass += ''.join(integers)
if 'д' in is_upper:
    first_pass += ''.join(characters1)
if 'д' in is_lower:
    first_pass += ''.join(characters2)
if 'д' in special_symbols:
    first_pass += ''.join(spec_symbols)
pass_gen(pass_count, pass_range, first_pass)

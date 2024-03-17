def ab(string):
    a = 'aeiouyAEIOUYаеіоиєуяюАЕІОИЄУЯЮ'
    b = 0
    for char in string:
        if char in a:
            b += 1
    return b

input_string = input("Введіть рядок: ")
print("Кількість голосних букв у рядку:", ab(input_string))
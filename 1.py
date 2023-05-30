print('введите число')
N = input()
N = int(N)
x = [1, 2, 4, 5, 9]
if N in x:
    print(x, N, 'Поздравляю, Вы угадали число!')
else:
    print(x, N, 'Нет такого числа!')

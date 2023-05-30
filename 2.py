print('повторяющиеся числа:')
list = [313, 4, 2, 3, 3, 33, 44, 45, 45, 45]
a = {str(x) for x in list if list.count(x) > 1}
x = lambda: print('')
y = lambda: print(' '.join(a))
x() \
    if len(a) < 1 else y()

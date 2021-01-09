f = open('1.txt')
ints = []
try:
    for line in f:
        ints.append(int(line))
    except ValueError:
        print('Это не число. Выходим.')
    except Exception:
        print('Это что ещё такое?')
    else:
        print('Всё хорошо.')
    finally:
        f.close()
        print('Я закрыл файл.')
import os
import os.path


def showCatalog():
    a = os.listdir(os.getcwd())
    a = str(a)
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace(" ", "")
    a = a.replace("'", "")
    a = a.replace(",", ", ")
    print('В вашем директории находятся:', a)


def moveUp():
    a = (os.path.split(os.getcwd()))[0]
    os.chdir(a)


def moveDown():
    a = input('Введите название папки: ')
    if os.path.isfile(os.path.join(os.getcwd(), a)):
        a = input('Вы ввели название файла, а не папки. Пожалуйста, повтрите попытку: ')
    while a not in os.listdir(os.getcwd()):
        a = input('Данной папки в текущей директории не обнаруженно. Пожалуйста, повторите попытку: ')
    b = os.path.join(os.getcwd(), a)
    os.chdir(b)


def countBytes(path):
    counter = 0
    _list_ = os.listdir(path)
    try:
        for i in _list_:
            if os.path.isfile(os.path.join(path, i)):
                counter += os.path.getsize(os.path.join(path, i))
            elif os.path.isdir(os.path.join(path, i)):
                counter += os.path.getsize(os.path.join(path, i))
                counter += countBytes(os.path.join(path, i))
    except PermissionError:
        pass
    return counter

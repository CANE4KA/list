from lisst import *
def func(*args) -> NoReturn:
    count = 0
    dictcc = {}
    for i in args:
        list0 = [funs(i, "bin"), funs(i, "octal"), funs(i, "dec"), funs(i, "hex")]
        dictcc[f"list{count}"] = list0
        count += 1
    for key, value in dictcc.items():
        lst1 = [2, 8, 10, 16]
        counter = 0
        print(f"Начало {key}")
        for ii in lst1:
            print(f"Значение в {ii}-ой СС: {dictcc[key][counter]}")
            counter += 1
        print(f"Конец {key}", end="\n\n")


func(123678678678)

def proverka(tuple):
    return all(tuple)
#all -> функция-проверка на истинность всех элемнтов тупла(кортежа)
example = [] 
a = int(input("Введите количество элементов,принимающих значения True/False , а после и их вовсе : "))
for i in range(a) :
    dimon = int(input()) 
    example.append(dimon)
print(proverka(example))

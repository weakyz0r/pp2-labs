import os
#ex1
# Write a Python program to list only directories, files and all directories, files in a specified path.
import os
def checking(path):
    directories = []  
    files = []  
    #listdir - возвращает список имен файлов и директорий, содержащихся в указанной директории
    #join - объединение путей файлов 
    for item in os.listdir(path):
        item_path = os.path.join(path, item) 

        if os.path.isdir(item_path):
            directories.append(item)  
        else:
            files.append(item) 

    print("Директории:")
    print('\n'.join(directories))

    print("\nФайлы:")
    print('\n'.join(files))

    print("\nВсе элементы:")
    print('\n'.join(os.listdir(path)))

path = input("Введите нужный путь: ")

checking(path)


#ex2
#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os
def checking (path):
    
    if os.path.exists(path):
        print(f"Путь {path} существует")
    else:
        print(f"Путь {path} не существует")
        return


    if os.access(path, os.R_OK):
        print(f"Путь {path} доступен для чтения")
    else:
        print(f"Путь {path} не доступен для чтения")

    # Проверка доступности файла для записи.
    if os.access(path, os.W_OK):
        print(f"Путь {path} доступен для записи")
    else:
        print(f"Путь {path} не доступен для записи")

    # Проверяем выполнимость пути 
    if os.access(path, os.X_OK):
        print(f"Путь {path} доступен для выполнения")
    else:
        print(f"Путь {path} не доступен для выполнения")

path = (input("Введите путь : "))
checking(path)


#ex3
#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

def checking (path):

    if os.path.exists(path):
        print(f"Путь {path} существует")

        dir_name = os.path.dirname(path) 
        file_name = os.path.basename(path)  

        print(f"Имя файла: {file_name}")
        print(f"Каталог: {dir_name}")
    else:
        print(f"Путь {path} не существует")


path = input("Введите путь: ")
checking(path)


#os.path.basename - возвращает имя файла из указанного пути
#os.path.dirname - возвращает имя каталога из указанного пути



#ex4
# Write a Python program to count the number of lines in a text file.

def counter(file_path):
    try:
        with open(file_path, 'r') as file:
            kolvo = sum(1 for line in file)
        print(f"Кол-во строк в файле {file_path}: {kolvo}")
    except FileNotFoundError as unlucky:
        print(f"Файл {file_path} не найден ;( ")


file_path = input("Введите путь к текстовому файлу: ")
counter(file_path)



#FileNotFoundError - тип исключения , когда файл не может быть найден :c
#конструкция with -> чтобы автоматически закрыть файл после выполнения блока кода.
#конструкция try-except в Python позволяет обработать исключения, которые могут возникнуть в блоке кода 
#и выполнить альтернативные действия в случае их возникновения.



#except Exception as e:
#    print(f"Произошел error : {e}")







#ex5
# Write a Python program to write a list to a file.

def writer(file_path, list):
    try:
        with open(file_path, 'w') as file:
            # Записываем каждый элемент списка в файл
            for item in list:
                file.write(str(item) + '\n')
                #file.write(','.join(list))
        print(f"Список успешно записан в файл {file_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


#list = ['pp2', 'is', 'the', 'best', 'subject']
list = input("Введите элементы списка : ").split(',')


file_path = input("Введите путь к файлу: ")
writer(file_path, list)


#split - расколоть/разбить (eng)



#ex6
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

def sozdavalka():
    letters = string.ascii_uppercase
    #metod ascii_uppercase возвращает строку, содержащую все заглавные буквы английского алфавита.
    
    for letter in letters:
        file_name = letter + ".txt"  
        with open(file_name, 'w') as file:  
            file.write(f"Content of {file_name}")  # Записываем в файл строку с содержимым

sozdavalka()




#ex7
# Write a Python program to copy the contents of a file to another file


def copy(source_file, result_file):
    try:
        with open(source_file, 'r') as source:
            # Читаем содержимое исходного файла
            content = source.read()

        with open(result_file, 'w') as result:
            # Записываем содержимое исходного файла в целевой файл
            result.write(content)
        
        print(f"Содержимое успешное скопировано :)")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


source_file = input("Введите путь к изначальному файлу ")
result_file = input("Введите путь к итоговому файлу: ")

copy(source_file, result_file)


#read,write - это методы объектов файлов :)





#ex8
# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.





import os
def delete(file_path):
    try:
        if os.path.exists(file_path):
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"Файл {file_path} был удален :) ")
            else:
                print(f"У вас нет доступа для удаления файла {file_path}")
        else:
            print(f"Файл {file_path} не существует")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = input("Введите путь к файлу : ")
delete(file_path)

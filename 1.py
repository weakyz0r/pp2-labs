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

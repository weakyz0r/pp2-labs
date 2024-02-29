from datetime import datetime, timedelta

current_date = datetime.now()

five_days_ago = current_date - timedelta(days=5)

print("Текущая дата:", current_date)
print("Пять дней назад было:", five_days_ago)



# # Запрос ввода даты у пользователя
# input_date_str = input("Введите дату в формате ГГГГ.ММ.ДД: ")

# # Преобразование строки в объект datetime
# input_date = datetime.strptime(input_date_str, "%Y.%m.%d")

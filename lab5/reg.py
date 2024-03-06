import re
f = open('row.txt','r', encoding='utf-8')
date = f.read()
x=re.findall("о.?п", date) # работает
print(x)

#1) Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
#findall - Возвращает список, содержащий все совпадения
#split - функция возвращает список, в котором строка была разделена при каждом совпадении
#sub - заменяет совпадения текстом по вашему выбору
#.span() возвращает кортеж, содержащий начальную и конечную позиции совпадения.
#.string возвращает строку, переданную в функцию
#.group() возвращает часть строки, в которой было совпадение

test1 ="aqua abobus abbus abberation"
#test1 = input("Введите строку: ")
x=re.findall(r"\S*ab*\S*", test1)
print(x)

#\S*: Ноль или более любых символов, кроме пробелов.
#

#2) Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
test1 ="aaqua aaabobus aabbus aabbberation"
x=re.findall(r"\S*ab{2,3}\S*", test1)
print(x)

#3) Write a Python program to find sequences of lowercase letters joined with a underscore.

test1 ="discrete_math_x low_case low"
x=re.findall(r"\S*[a-z]+_[a-z]+\S*", test1)
print(x)


#4) Write a Python program to find the sequences of one upper case letter followed by lower case letters.



test1 ="Discrete math"
x=re.findall(r"\S*[A-Z][a-z]\S*", test1)
print(x)


#5) Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
test1 ="aqweb aqwea"
test2 = "saqweb"
x = re.findall(r".a.*b", test1)
print(x)


#6) Write a Python program to replace all occurrences of space, comma, or dot with a colon.

test1 = "Night we meet, i see you."
x = re.sub("[.,\s]", ":", test1)
print(x)

#7) Write a python program to convert snake case string to camel case string.

test1 = "snake_people"
x = re.sub(r'_([\w])', lambda x: x.group(1).upper(), test1)
print(x)

#snake - my_home ; my_various ; low_case myHome
#camel - myClassHome ; myHome ; myRound 

#snake_case_string = "my_variable_name"
#camel_case_string = snake_to_camel(snake_case_string)
#print(camel_case_string)  # Output: "myVariableName"


#8) Write a Python program to split a string at uppercase letters.
test1 = "RinNot."
x = re.findall(r'[A-Z][^A-Z]*', test1)
print(x)

#9) Write a Python program to insert spaces between words starting with capital letters.

test1 = "NeverBeLate"
x = re.sub(r'(\w)([A-Z])', lambda x: x. group(1) + " " + x.group(2), test1)
print(x)

#10) Write a Python program to convert a given camel case string to snake case.

test1 = "neverGonnaGiveYouUp"
x = re.sub(r'(\w)([A-Z])', lambda x: x. group(1) + "_" + x.group(2).lower(), test1)
print(x)
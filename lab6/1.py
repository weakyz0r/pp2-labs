def multiplication(numbers):
    result = 1
    for chislo in numbers:
        result *= chislo
    return result

my_list = [] 
a = int(input("Введите количество чисел , а после и их вовсе : "))
for i in range(a) :
    dimon = int(input()) 
    my_list.append(dimon)

result = multiplication(my_list)

print("List multiplication is" , result)
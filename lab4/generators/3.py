def divisible_by_3_and_4_generator(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Введите число N: "))
numbers = divisible_by_3_and_4_generator(n)
for num in numbers:
    print(num)

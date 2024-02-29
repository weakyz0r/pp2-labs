def schetchik(n):
    while n >= 0:
        yield n
        n= n-1

n = int(input("Vvedite chislo n :"))

schetchik1 = schetchik(n)
for num in schetchik1:
    print(num)


# n = int(input("Введите число n: "))

# while n >= 0:
#     print(n)
#     n -= 1

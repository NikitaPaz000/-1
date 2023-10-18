def generate_fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = int(input("Введите количество чисел Фибоначчи: "))

for number in generate_fibonacci(n):
    print(number)

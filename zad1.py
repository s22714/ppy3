numery = input("Podaj liczby oddzielone przecinkami: ")

numbers = numery.split(",")
min = numbers[0]
max = numbers[0]
for n in numbers:
    if int(min) > int(n):
        min = n
    if int(max) < int(n):
        max = n

##print(numbers)

print("Max => " + max)
print("Min => " + min)


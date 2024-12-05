first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
count = 1

if first == second and first == third:
    count += 2
elif first == second or first ==third or second == third:
    count += 1
else:
    count = 0
print ("Кол-во одинаковых чисел: ", count)
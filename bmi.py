# Расчёт индекса массы тела
print('Привет дорогой Гость, давай познакомимся! Напиши своё имя: ')

name = input()

print("Привет, ", name, "!")

age = int(input("Сколько Вам полных лет? "))

height = float(input("Ваш рост? "))

weight = float(input("Ваш вес? "))

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:

    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2

    bmi = round(bmi, 2)

    print("Ваш индекс массы тела: ", str(bmi))

    if age < 45 and bmi < 18.5 or age >= 45 and bmi < 22:
        description = 'недостаточной массой тела.'
    elif age < 45 and bmi < 24.99 or age >= 45 and bmi < 26.99:
        description = 'нормальной массой тела.'
    elif age < 45 and bmi < 29.99 or age >= 45 and bmi < 31.99:
        description = 'избыточной массой тела.'
    else:
        description = 'ожирением.'
    print("bmi=", bmi, "Вы относитесь к группе людей с", description)

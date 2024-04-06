weight = float(input("Введите ваш вес в фунтах: "))
height = float(input("Введите ваш рост в дюймах: "))

bmi = 703 * weight / height ** 2
print("Ваш индекс массы тела (ИМТ): {:.2f}".format(bmi))
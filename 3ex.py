prices = input("Введите цены двух шоколадок через пробел: ")

S, R = map(int, prices.split())

total_cost = S + R

print("Общая стоимость двух шоколадок: ", total_cost, "рублей")

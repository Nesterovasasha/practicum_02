def meters_to_miles(meters):
    miles = meters * 0.000621371
    return miles

distance_in_meters = float(input("Введите расстояние, которое преодолела Фейт в метрах: "))
distance_in_miles = meters_to_miles(distance_in_meters)
print(f"Фейт пробежала {distance_in_miles} миль.")

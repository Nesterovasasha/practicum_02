def calculate_rain_volume(ha_area, rainfall_cm):
    cubic_meter_per_hectare = 10000
    rain_volume_liters = ha_area * rainfall_cm * cubic_meter_per_hectare
    return rain_volume_liters

hectare_area = 1
rainfall = 1

rain_volume = calculate_rain_volume(hectare_area, rainfall)
print("Объем дождя на один гектар: {} литров".format(rain_volume))

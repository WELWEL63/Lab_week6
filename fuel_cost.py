def fuel_cost(distance_miles):
#     # Constants
     MPG = 50  # Miles per gallon
     LITERS_PER_GALLON = 4.5
     PRICE_PER_LITER = 1.49  # Price in pounds per liter
#     continue function implementation here...
     total_fuel_cost = (distance_miles/MPG) * LITERS_PER_GALLON * PRICE_PER_LITER

     return total_fuel_cost

print(fuel_cost(500))
print(fuel_cost(510))
print(fuel_cost(150))
print(fuel_cost(50))
print(fuel_cost(600))
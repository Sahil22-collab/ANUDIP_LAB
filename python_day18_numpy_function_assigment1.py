# Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).


import numpy as np

# List of temperatures for each day
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4, 25, 12, -4, -12])

# Find hot days (above 35°C)
hot_days = np.where(temperatures > 35)

# Find cold days (below 5°C)
cold_days = np.where(temperatures < 5)

# Display hot and cold days
print(f"Hot days : {hot_days[0]}")
print(f"Temperatures on hot days: {temperatures[hot_days]}")

print(f"Cold days : {cold_days[0]}")
print(f"Temperatures on cold days: {temperatures[cold_days]}")

'''
output
Hot days : [2 5 9]
Temperatures on hot days: [36.8 38.7 37.2]
Cold days : [10 13 14]
Temperatures on cold days: [  4.  -4. -12.]'''



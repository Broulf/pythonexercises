temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
wind_speed = eval(input("Enter the wind speed in miles per hour: "))
wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** .16)) + (0.4275 * temperature * (wind_speed ** 0.16))

if temperature < -58:
    print("The temperature is too low")
elif temperature > 41:
    print("The temperature is too high")
elif wind_speed < 2:
    print("The wind is to light")
else:
    print("The wind chill index is", wind_chill)
def weather_condition(temperature):
    if temperature>7:
        return "Warm"
    else:
        return "Cold"


temp = int(input("Enter temperature : "))
print(weather_condition(temp))


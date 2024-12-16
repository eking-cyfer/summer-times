
temperature = float(input("Enter the current temperature in Celsius: "))

if temperature >= 25:
    print("It's hot! Wear light clothes.")
elif temperature >= 15:
    print("Mild weather. A light jacket might be good.")
elif temperature >= 5:
    print("It's chilly. Wear a pullover or light jacket.")
else:
    print("It's cold! Wear warm clothes like a jacket and pullover.")

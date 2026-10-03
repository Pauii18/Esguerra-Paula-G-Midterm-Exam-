def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    # New conversion class: Fahrenheit to Celsius
    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9

    # New conversion class: Kelvin to Celsius
    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    # 1. Celsius Conversions
    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")
    print("-" * 30)

    # 2. Fahrenheit Conversion
    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")
    print("-" * 30)

    # 3. Kelvin Conversion
    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")

main()

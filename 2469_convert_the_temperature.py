class Solution:
    def convert(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.80) + 32.00
        return [kelvin, fahrenheit]

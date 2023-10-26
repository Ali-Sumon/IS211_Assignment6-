def convertCelsiusToKelvin(celsius):
    """
    Convert Celsius to Kelvin.
    Formula: kelvin = celsius + 273.15
    :param celsius: Temperature in Celsius
    :return: Temperature in Kelvin
    """
    if celsius < -273.15:
        raise ValueError("Temperature in Celsius cannot be below absolute zero.")
    kelvin = celsius + 273.15
    return kelvin


def convertCelsiusToFahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: fahrenheit = (celsius * 9/5) + 32
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def convertFahrenheitToCelsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: celsius = (fahrenheit - 32) * 5/9
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin.
    Formula: kelvin = (fahrenheit + 459.67) * 5/9
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Kelvin
    """
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin


def convertKelvintoFahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit.
    Formula: fahrenheit = (kelvin * 9/5) - 459.67
    :param kelvin: Temperature in Kelvin
    :return: Temperature in Fahrenheit
    """
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit


def convertKelvintoCelsius(kelvin):
    """
    Convert Kelvin to Celsius.
    Formula: celsius = kelvin - 273.15
    :param kelvin: Temperature in Kelvin
    :return: Temperature in Celsius
    """
    celsius = kelvin - 273.15
    return celsius

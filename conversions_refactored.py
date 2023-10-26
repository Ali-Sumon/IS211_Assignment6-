import argparse


class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    """
    Converts between Fahrenheit, Celsius, and Kelvin, as well as between Miles, Yards, and Meters.
    :param fromUnit: The unit to convert from (string)
    :param toUnit: The unit to convert to (string)
    :param value: The value to convert (float)
    :return: The converted value (float)
    """

    # Check if units are compatible
    temperature_units = ['CELSIUS', 'FAHRENHEIT', 'KELVIN']
    distance_units = ['YARDS', 'METERS', 'MILES']

    if fromUnit.upper() not in temperature_units and fromUnit.upper() not in distance_units:
        raise ConversionNotPossible(f"Conversion from {fromUnit.upper()} is not possible.")

    if toUnit.upper() not in temperature_units and toUnit.upper() not in distance_units:
        raise ConversionNotPossible(f"Conversion to {toUnit.upper()} is not possible.")

    if fromUnit.upper() in temperature_units and toUnit.upper() in distance_units:
        raise ConversionNotPossible(f"Conversion between {fromUnit.upper()} and {toUnit.upper()} is not possible.")

    if fromUnit.upper() in distance_units and toUnit.upper() in temperature_units:
        raise ConversionNotPossible(f"Conversion between {fromUnit.upper()} and {toUnit.upper()} is not possible.")

    # Return the same value if units are the same
    if fromUnit.upper() == toUnit.upper():
        return value

    # Temperature Conversions
    if fromUnit.upper() == 'CELSIUS' and toUnit.upper() == 'KELVIN':
        convertedValue = value + 273.15
        return convertedValue

    if fromUnit.upper() == 'CELSIUS' and toUnit.upper() == 'FAHRENHEIT':
        convertedValue = (value * 9 / 5) + 32
        return convertedValue

    if fromUnit.upper() == 'FAHRENHEIT' and toUnit.upper() == 'CELSIUS':
        convertedValue = (value - 32) * 5 / 9
        return convertedValue

    if fromUnit.upper() == 'FAHRENHEIT' and toUnit.upper() == 'KELVIN':
        convertedValue = (value + 459.67) * 5 / 9
        return convertedValue

    if fromUnit.upper() == 'KELVIN' and toUnit.upper() == 'FAHRENHEIT':
        convertedValue = (value * 9 / 5) - 459.67
        return convertedValue

    if fromUnit.upper() == 'KELVIN' and toUnit.upper() == 'CELSIUS':
        convertedValue = value - 273.15
        return convertedValue

    # Distance Conversions
    if fromUnit.upper() == 'YARDS' and toUnit.upper() == 'METERS':
        convertedValue = value * 0.9144
        return convertedValue

    if fromUnit.upper() == 'YARDS' and toUnit.upper() == 'MILES':
        convertedValue = value / 1760
        return convertedValue

    if fromUnit.upper() == 'METERS' and toUnit.upper() == 'YARDS':
        convertedValue = value * 1.093613
        return convertedValue

    if fromUnit.upper() == 'METERS' and toUnit.upper() == 'MILES':
        convertedValue = value / 1609.344
        return convertedValue

    if fromUnit.upper() == 'MILES' and toUnit.upper() == 'YARDS':
        convertedValue = value * 1760
        return convertedValue

    if fromUnit.upper() == 'MILES' and toUnit.upper() == 'METERS':
        convertedValue = value * 1609.344
        return convertedValue


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert temperature and distance units')
    parser.add_argument('fromUnit', type=str, help='Unit to convert from')
    parser.argument('toUnit', type=str, help='Unit to convert to')
    parser.add_argument('value', type=float, help='Temperature or distance value to convert')
    args = parser.parse_args()

    # Call the conversion function with the provided arguments
    result = convert(args.fromUnit, args.toUnit, args.value)

    # Print the result of the conversion
    print(f"{args.value} {args.fromUnit} is equal to {result} {args.toUnit}")


if __name__ == '__main__':
    main()

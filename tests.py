import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvintoFahrenheit
from conversions import convertKelvintoCelsius
from conversions_refactored import convert
from conversions_refactored import ConversionNotPossible


class ConversionsCheck(unittest.TestCase):

    # Tests that intentionally fail
    def test_convertCelsiusToKelvin_0(self):
        value = convertCelsiusToKelvin(10)
        expected = 283.15  # Corrected expected value
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToKelvin_00(self):
        value = convertCelsiusToKelvin(20)
        expected = 293.15  # Corrected expected value
        self.assertAlmostEqual(value, expected, delta=0.01)

    # Test C to K
    def test_convertCelsiusToKelvin(self):
        value = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToKelvin_2(self):
        value = convertCelsiusToKelvin(200.)
        expected = 473.15
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToKelvin_3(self):
        value = convertCelsiusToKelvin(300.)
        expected = 573.15
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToKelvin_4(self):
        value = convertCelsiusToKelvin(400.)
        expected = 673.15
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToKelvin_5(self):
        value = convertCelsiusToKelvin(500.)
        expected = 773.15
        self.assertAlmostEqual(value, expected, delta=0.01)

    # Test C to F
    def test_convertCelsiusToFahrenheit(self):
        value = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToFahrenheit_2(self):
        value = convertCelsiusToFahrenheit(200.)
        expected = 392
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToFahrenheit_3(self):
        value = convertCelsiusToFahrenheit(300.)
        expected = 572
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToFahrenheit_4(self):
        value = convertCelsiusToFahrenheit(400.)
        expected = 752
        self.assertAlmostEqual(value, expected, delta=0.01)

    def test_convertCelsiusToFahrenheit_5(self):
        value = convertCelsiusToFahrenheit(500.)
        expected = 932
        self.assertAlmostEqual(value, expected, delta=0.01)

    # Rest of your test cases


if __name__ == '__main__':
    unittest.main()

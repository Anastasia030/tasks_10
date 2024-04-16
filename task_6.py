import re


class RomanNumber:
    """
    Roman Number Class
    """
    def __init__(self, number):
        """
        A method that defines an instance of a Roman number record
        :param number: a string with a Roman number entry
        """
        if isinstance(number, int) or (isinstance(number, float) and number.is_integer()):
            number = int(number)
            if 0 < number < 4000:
                self.int_value = number
                self.rom_value = self.roman_number()
            else:
                print('error')
                self.int_value = None

        elif isinstance(number, str):
            if re.match('^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$', number) is None:
                print('error')
                self.rom_value = None
            else:
                self.rom_value = number
                self.int_value = self.decimal_number()
        else:
            print('error')
            self.rom_value = None
            self.int_value = None

    def decimal_number(self):
        """
        A method that converts a Roman number to decimal
        :return: a number indicating the decimal equivalent
        """
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        if self.rom_value is not None:
            for letter in self.rom_value:
                value = roman_numerals[letter]
                if value > prev_value:
                    result += value - 2 * prev_value
                else:
                    result += value
                prev_value = value

            return result
        return self.rom_value

    def roman_number(self):
        """
        A method that translates into the Roman system
        :return: A string is the equivalent of a number in the Roman numeral system
        """
        if self.int_value is not None:
            number = self.int_value
            roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                              9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
            result = ''
            for val, numeral in roman_numerals.items():
                count = number // val
                result += numeral * count
                number -= val * count

            return result
        return None

    @staticmethod
    def is_roman(value):
        """
        A statistical method that checks whether a number is Roman
        :param value: the number that we are checking
        :return: logical expression
        """
        if re.match('^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$', value) is None:
            return False
        else:
            return True

    @staticmethod
    def is_int(value):
        """
        A statistical method that checks whether a number is representable by Roman
        :param value: the number that we are checking
        :return: logical expression
        """
        if isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
            if 0 < value < 4000:
                return True
            else:
                return False

    def __add__(self, other):
        """
        The method of redefining the addition operation
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            result = self.int_value + other.int_value
            return RomanNumber(result)
        else:
            print('error')
            return RomanNumber(None)

    def __sub__(self, other):
        """
        The method of redefining the subtraction operations
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            result = self.int_value - other.int_value
            return RomanNumber(result)
        else:
            print('error')
            return RomanNumber(None)

    def __mul__(self, other):
        """
        The method of redefining the multiplication operations
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            result = self.int_value * other.int_value
            return RomanNumber(result)
        else:
            print('error')
            return RomanNumber(None)

    def __truediv__(self, other):
        """
        The method of redefining the division operations
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            result = self.int_value / other.int_value
            if result.is_integer():
                return RomanNumber(result)
            else:
                return RomanNumber(None)
        else:
            print('error')
            return RomanNumber(None)

    def __floordiv__(self, other):
        """
        The method of redefining the integer division operation
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            result = self.int_value // other.int_value
            return RomanNumber(result)
        else:
            print('error')
            return RomanNumber(None)

    def __mod__(self, other):
        """
        The method of redefining the remainder from division operations
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            result = self.int_value % other.int_value
            return RomanNumber(result)
        else:
            print('error')
            return RomanNumber(None)

    def __pow__(self, power, modulo=None):
        """
        The method of redefining the exponentiation operations
        :param power: the number with which the operation is performed
        :param modulo: the number of calculating the remainder of the division of the exponentiation result
        :return: the number with the result of the operation
        """
        if isinstance(power, RomanNumber):
            result = self.int_value ** power.int_value
            return RomanNumber(result)
        else:
            print('error')
            return RomanNumber(None)

    def __str__(self):
        """
        The method outputs a string with a Roman number
        :return: string with a Roman number
        """
        return f'{self.rom_value}'

    def __repr__(self):
        """
        The method outputs a string with a Roman number
        :return: string with a Roman number
        """
        return self.__str__()

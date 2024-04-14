import roman


class RomanNumber:
    """
    Roman Number Class
    """

    def __init__(self, number):
        """
        A method that defines an instance of a number record
        :param number: a string with a Roman number entry or a number
        """
        if isinstance(number, int):
            try:
                self.rom_value = roman.toRoman(number)
                self.int_value = number

            except roman.OutOfRangeError:
                print('mistake')
                self.int_value = None
        else:
            try:
                self.int_value = roman.fromRoman(number)
                self.rom_value = number

            except roman.InvalidRomanNumeralError:
                print('mistake')
                self.rom_value = None

    def decimal_number(self):
        """
        A method that converts a Roman number to decimal
        :return: a number indicating the decimal equivalent
        """
        return roman.fromRoman(self.rom_value)

    def roman_number(self):
        """
        A method that translates into the Roman system
        :return: A string is the equivalent of a number in the Roman numeral system
        """
        number = roman.toRoman(self.int_value)
        return f'{number}'

    @staticmethod
    def is_roman(value):
        """
        A statistical method that checks whether a number is Roman
        :param value: the number that we are checking
        :return: logical expression
        """
        try:
            value_number = roman.fromRoman(value)

        except roman.InvalidRomanNumeralError:
            value_number = None

        return isinstance(value_number, int)

    @staticmethod
    def is_int(value):
        """
        A statistical method that checks whether a number is representable by Roman
        :param value: the number that we are checking
        :return: logical expression
        """
        try:
            value_number = roman.toRoman(value)

        except roman.OutOfRangeError:
            value_number = None

        return isinstance(value_number, str)

    def __add__(self, other):
        """
        The method of redefining the addition operation
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            try:
                result = roman.toRoman(self.int_value + other.int_value)
                return RomanNumber(result)
            except roman.OutOfRangeError:
                print('mistake')
                result = RomanNumber(None)
                return result

    def __sub__(self, other):
        """
        The method of redefining the subtraction operations
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            try:
                result = roman.toRoman(self.int_value - other.int_value)
                return RomanNumber(result)
            except roman.OutOfRangeError:
                print('mistake')
                result = RomanNumber(None)
                return result

    def __mul__(self, other):
        """
        The method of redefining the multiplication operations
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            try:
                result = roman.toRoman(self.int_value * other.int_value)
                return RomanNumber(result)
            except roman.OutOfRangeError:
                print('mistake')
                result = RomanNumber(None)
                return result

    def __truediv__(self, other):
        """
        The method of redefining the division operations
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            try:
                result = self.int_value / other.int_value
                if result.is_integer():
                    result = roman.toRoman(int(result))
                    return RomanNumber(result)
                else:
                    return RomanNumber(None)

            except roman.OutOfRangeError:
                print('mistake')
                result = RomanNumber(None)
                return result

    def __floordiv__(self, other):
        """
        The method of redefining the integer division operation
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            try:
                result = roman.toRoman(self.int_value // other.int_value)
                return RomanNumber(result)
            except roman.OutOfRangeError:
                print('mistake')
                result = RomanNumber(None)
                return result

    def __mod__(self, other):
        """
        The method of redefining the remainder from division operations
        :param other: the number with which the operation is performed
        :return: the number with the result of the operation
        """
        if isinstance(other, RomanNumber):
            try:
                result = roman.toRoman(self.int_value % other.int_value)
                return RomanNumber(result)
            except roman.OutOfRangeError:
                print('mistake')
                result = RomanNumber(None)
                return result

    def __pow__(self, power, modulo=None):
        """
        The method of redefining the exponentiation operations
        :param power: the number with which the operation is performed
        :param modulo: the number of calculating the remainder of the division of the exponentiation result
        :return: the number with the result of the operation
        """
        if isinstance(power, RomanNumber):
            try:
                result = roman.toRoman(self.int_value ** power.int_value)
                return RomanNumber(result)
            except roman.OutOfRangeError:
                print('mistake')
                result = RomanNumber(None)
                return result

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

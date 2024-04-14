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

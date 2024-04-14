import roman


class RomanNumber:
    """
    Roman Number Class
    """
    def __init__(self, roman_number):
        """
        A method that defines an instance of a Roman number record
        :param roman_number: a string with a Roman number entry
        """
        try:
            roman.fromRoman(roman_number)
            self.rom_value = roman_number

        except roman.InvalidRomanNumeralError:
            print('mistake')
            self.rom_value = None

    def decimal_number(self):
        """
        A method that converts a Roman number to decimal
        :return: a number indicating the decimal equivalent
        """
        return roman.fromRoman(self.rom_value)

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

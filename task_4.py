import re


class RomanNumber:
    """
    Roman Number Class
    """
    def __init__(self, roman_number):
        """
        A method that defines an instance of a Roman number record
        :param roman_number: a string with a Roman number entry
        """
        if re.match('^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$', roman_number) is None:
            print('error')
            self.rom_value = None
        else:
            self.rom_value = roman_number

    def decimal_number(self):
        """
        A method that converts a Roman number to decimal
        :return: a number indicating the decimal equivalent
        """
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for letter in self.rom_value:
            value = roman_numerals[letter]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value

        return result

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

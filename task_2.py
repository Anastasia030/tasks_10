class NavalBattle:
    """
    The class of the game "Sea Battle"
    """
    playing_field = []

    def __init__(self, symbol):
        """
        A method that defines an instance of player characters
        :param symbol: a string with the player's symbol
        """
        self.symbol = symbol

    @staticmethod
    def show():
        """
        A statistical method that displays the playing field under the hiding symbol
        """
        for string in NavalBattle.playing_field:
            battle_line = ''
            for cell in string:
                if cell == 1 or cell == 0:
                    battle_line += '~'
                else:
                    battle_line += cell
            print(battle_line)

    def shot(self, x, y):
        """
        The method by which the players walk and determines whether the player is hit
        :param x: the number indicating the horizontal coordinate
        :param y: the number indicating the vertical coordinate
        """
        if NavalBattle.playing_field[y-1][x-1] == 0:
            NavalBattle.playing_field[y-1][x-1] = 'o'
            print('мимо')
        if NavalBattle.playing_field[y-1][x-1] == 1:
            NavalBattle.playing_field[y-1][x-1] = self.symbol
            print('попал')

    def __str__(self):
        """
        The method outputs a string with the player's symbol
        :return: string with the player's symbol
        """
        return f"The player's symbol: {self.symbol}"

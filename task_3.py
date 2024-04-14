import random


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
        if not NavalBattle.playing_field:
            print('игровое поле не заполнено')

        elif NavalBattle.playing_field[y - 1][x - 1] == 0:
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
            print('мимо')

        elif NavalBattle.playing_field[y - 1][x - 1] == 1:
            NavalBattle.playing_field[y - 1][x - 1] = self.symbol
            print('попал')

        else:
            print('ошибка')

    @classmethod
    def new_game(cls):
        """
        A statistical method that creates a playing field and places ships on it randomly
        """

        while True:
            count_ships = [0, 0, 0, 0]
            NavalBattle.playing_field = [[0 for _ in range(10)] for _ in range(10)]
            ships = (3, 2, 2, 1, 1, 1)

            for cells in range(4):
                x, y = random.randint(0, 9), random.randint(0, 9)

                NavalBattle.playing_field[y][x] = 1

            for cells in ships:
                x, y = random.randint(0, 9), random.randint(0, 9)
                NavalBattle.playing_field[y][x] = cells + 1
                x_or_y = random.randint(0, 1)
                next_cell = random.choice([-1, 1])
                cell = 0

                while cell != cells:
                    if x_or_y == 0:
                        x = x + next_cell
                        if x < 0 or x > 9:
                            cell = -1
                            NavalBattle.playing_field = [[0 for _ in range(10)] for _ in range(10)]
                            x, y = random.randint(0, 9), random.randint(0, 9)
                        else:
                            NavalBattle.playing_field[y][x] = cells + 1
                            cell += 1

                    else:
                        y = y + next_cell

                        if y < 0 or y > 9:
                            cell = -1
                            NavalBattle.playing_field = [[0 for _ in range(10)] for _ in range(10)]
                            x, y = random.randint(0, 9), random.randint(0, 9)
                        else:
                            NavalBattle.playing_field[y][x] = cells + 1
                            cell += 1

            for battle_line in NavalBattle.playing_field:
                for cell in battle_line:
                    if cell == 1:
                        count_ships[0] += 1
                    elif cell == 2:
                        count_ships[1] += 1
                    elif cell == 3:
                        count_ships[2] += 1
                    elif cell == 4:
                        count_ships[3] += 1

            mistake = 0
            for y in range(10 - 1):
                for x in range(10 - 1):
                    if NavalBattle.playing_field[y][x] != 0 and NavalBattle.playing_field[y][x + 1] != 0 and \
                            NavalBattle.playing_field[y][x] != NavalBattle.playing_field[y][x + 1]:
                        mistake += 1

            for x in range(10 - 1):
                for y in range(10 - 1):
                    if NavalBattle.playing_field[y][x] != 0 and NavalBattle.playing_field[y + 1][x] != 0 and \
                            NavalBattle.playing_field[y][x] != NavalBattle.playing_field[y + 1][x]:
                        mistake += 1

            if count_ships == [4, 6, 6, 4] and mistake == 0:
                break

        for x in range(10):
            for y in range(10):
                if NavalBattle.playing_field[y][x] != 0:
                    NavalBattle.playing_field[y][x] = 1

    def __str__(self):
        """
        The method outputs a string with the player's symbol
        :return: string with the player's symbol
        """
        return f"The player's symbol: {self.symbol}"

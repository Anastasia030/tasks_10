class Circle:
    """
    Circle class
    """
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=None):
        """
        The method that defines the instance
        :param radius: the number indicating the radius of the circle
        """
        self.radius = radius
        if radius is None:
            self.radius = 1
        Circle.all_circles.append(self.radius)

    def area(self):
        """
        A method that returns the area of a circle
        :return: the number with the area of the circle
        """
        square = Circle.pi * self.radius ** 2
        return square

    @staticmethod
    def total_area():
        """
        A statistical method that returns the total area of all instances of a class
        :return: a number indicating the total area
        """
        sum_square = 0
        for radius in Circle.all_circles:
            sum_square += (Circle.pi * radius ** 2)
        return sum_square

    def __str__(self):
        """
        The method outputs a string with the radius of the instance
        :return: string with the radius of the instance
        """
        return f'{self.radius}'

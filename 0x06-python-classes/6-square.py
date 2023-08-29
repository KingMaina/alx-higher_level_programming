class Square:
    """A square class"""

    __size = 3
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        x, y = position
        if (len(position) != 2 or x < 0 or y < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        x, y = value
        if len(value) != 2 or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()

class Road:
    _length = None
    _width = None
    __asphalt = 0.25
    __depth = 0.5

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calculate(self):
        return self._length * self._width * self.__asphalt * self.__depth
lenght = float(input('Введите длину : '))
width = float(input('Введите ширину: '))
road = Road(lenght, width)
print(f'Необходимо асфальта: {road.calculate()} т.')
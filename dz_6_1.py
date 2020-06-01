import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print('rafficLight on')

        self.__color = 'red'
        print(f'Set color: {self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'Set color: {self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f'Set color: {self.__color}')
        time.sleep(7)


traffic_light = TrafficLight()
print(traffic_light.running())

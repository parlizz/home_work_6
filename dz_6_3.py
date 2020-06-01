class Worker:
    name = None
    surname = None
    position = None
    _income = {
        'wage': 'wage',
        'bonus': 'bonus'
    }

class Position(Worker):
    def __init__(self, name:str, surname:str, wage:float, bonus:float):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

position = Position(name='Ivan', surname='Ivanov', wage=222.1, bonus=123.45)
print(f'Full Name: {position.get_full_name()}')
print(f'Total: {position.get_total_income()} p.')
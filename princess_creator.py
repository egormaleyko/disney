import re
import princess


class Princess_creator:

    def __init__(self):
        self.allowed_haircolors = ['black', 'blonde', 'platinum-blonde', 'strawberry-blonde', 'red', 'brown']
        self.allowed_eyecolor = ['brown', 'blue', 'violet', 'hazel']
        self.line_pattern = "(-?\d+)\s+([A-z\s]+)\s+(\d+)\s+([A-z-]+)\s+([A-z]+)"

    def create_princess(self, input):

        result = re.split(self.line_pattern, input)
        data = list(filter(None, result))

        if not self.__check_number(data[0]):
            print('Номер принцессы должен быть положительным')
            return None

        if not self.__check_name(data[1]):
            print('Размер имени не может привышать 30 символов')
            return None

        if not self.__check_age(data[2]):
            print('Возраст должен находится в промежутке от 0 до 99')
            return None

        if not self.__check_is_allowed_haircolor(data[3]):
            print('Неподходящий цвет волос')
            return None

        if not self.__check_is_allowed_eyecolor(data[4]):
            print('Неподходящий цвет глаз')
            return None

        return princess.Princess(data[0], data[1], data[2], data[3], data[4])

    def __check_number(self, number):
        return int(number) > 0

    def __check_name(self, name):
        return len(name) <= 30

    def __check_age(self, age):
        return 0 < int(age) < 99

    def __check_is_allowed_haircolor(self, haircolor):
        return str(haircolor).lower() in self.allowed_haircolors

    def __check_is_allowed_eyecolor(self, eyercolor):
        return str(eyercolor).lower() in self.allowed_eyecolor

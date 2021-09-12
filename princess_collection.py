class Princess_collection:
    def __init__(self):
        self.__princess_list = []

    def list(self):
        for princess in self.__princess_list:
            print(' ' + princess.number + '.' + princess.name, '\n',
                  'Age: ' + princess.age, '\n',
                  'Hair: ' + princess.haircolor, '\n',
                  'Eye: ' + princess.eyecolor, '\n')

    # TODO:добавить логику при наличии одинакрвы индексов
    def add(self, princess):
        if not self.__contains__(princess.number):
            self.__princess_list.append(princess)

    # TODO:добавить логику при наличии одинакрвы индексов
    def delete(self, number):
        if self.__contains__(number):
            princess = self.get(number)
            self.__princess_list.remove(princess)
        else:
            return -1

    def get(self, number):
        for princess in self.__princess_list:
            if princess.number == number:
                return princess
        return -1

    def update(self, princess):
        if self.__contains__(princess.number):
            old_princess = self.get(princess.number)
            self.__princess_list.remove(old_princess)
            self.add(princess)

    def __contains__(self, number):
        for princess in self.__princess_list:
            if princess.number == number:
                return True
        return False

import time


def openfile(filepath):
    file = open(filepath)
    values = file.read()
    return(values.replace('|', '').split())

def menu():
    print('''Что желаете выполнить? 
1. Прочитать файл
2. Добавить новый элемент
3. Удалить элемент
4. Изменить элемент
5. Завершить программу\n''''')


class Princess:
    def __init__(self, number, name, age, selfhaircolor, eyecolor):
        self.number = number
        self.name = name
        self.age = age
        self.selfhaircolor=selfhaircolor
        self.eyecolor=eyecolor

    def list(self):
        print(self.number+'. '+ self.name + '\n''Age: '+ self.age + '\n''Eye: ' + self.eyecolor +'\n''Hair: '+ self.selfhaircolor, '\n')

    def __del__(self):
        print('Princess delete')



filepath = openfile('disney.txt')

one = Princess(filepath[0],filepath[1]+' '+filepath[2],filepath[3], filepath[4], filepath[5])
two = Princess(filepath[6],filepath[7], filepath[8], filepath[9], filepath[10])
three = Princess(filepath[11],filepath[12], filepath[13], filepath[14], filepath[15])
four = Princess(filepath[16],filepath[17], filepath[18], filepath[19], filepath[20])
five = Princess(filepath[21],filepath[22], filepath[23], filepath[24], filepath[25])

info = 0
while info != 5:
    menu()
    info = int(input())
    if info == 1:
        one.list()
        two.list()
        three.list()
        four.list()
        five.list()




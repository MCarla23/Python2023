class Employee:
    def __init__(self, name, salary, hwork):
        self.name = name
        self.salary = salary
        self.hwork = hwork


class Manager(Employee):
    def __init__(self, name, salary, hwork, team, people):
        super().__init__(name, salary, hwork)
        self.team = team
        self.people = people

    def manages(self):
        print('The manager ' + self.name + ' manages team ' + self.team +
              '. The people in this team are: ' + self.people + '.')


class Engineer(Employee):
    def __init__(self, name, salary, hwork, project):
        super().__init__(name, salary, hwork)
        self.project = project

    def works(self):
        print('The engineer ' + self.name + ' works at project ' + self.project + '.')


class Salesperson(Employee):
    def __init__(self, name, salary, hwork, obj):
        super().__init__(name, salary, hwork)
        self.item = obj

    def sales(self):
        print('The salesperson ' + self.name + ' sales ' + self.item + '.')


edi = Manager('Eduard Kiff', '4500', '8','The purple ring', 'Luana, Andrei, Max, Maria')
lizz = Engineer('Elizabeth Keen', '3200', 4, 'The Blacklist')
harold = Salesperson('Harold Red', '8700', 12, 'guns')

edi.manages()
lizz.works()
harold.sales()
class Account:
    def __init__(self, id_person, name, balance = 0):
        self.id = id_person
        self.name = name
        self.balance = balance

    def deposit(self, money_to_deposit):
        if money_to_deposit > 0:
            self.balance += money_to_deposit
            print('Ati depus cu succes suma de ' + str(money_to_deposit) + '. Suma totala actuala: ' + str(self.balance))
        else:
            print('Tranzactie esuata.')

    def withdrawal(self, money_to_withdrawal):
        if money_to_withdrawal <= self.balance:
            self.balance -= money_to_withdrawal
            print('Ati retras cu succes suma de ' + str(money_to_withdrawal) + '. Suma totala actuala: ' + str(self.balance))
        else:
            print('Tranzactie esuata.')


class SavingsAccount(Account):
    def __init__(self,  id_person, name, balance, irate):
        super().__init__(id_person, name, balance)
        self.interestRate = irate

    def interest_calculation(self):
        self.balance += (self.balance * self.interestRate) / 100
        print('Rata dobanzii: ' + str(self.interestRate) + '. Suma totala actuala: ' + str(self.balance))
        return self.balance


class CheckingAccount(Account):
    def __init__(self,  id_person, name, balance, minim_balance):
        super().__init__(id_person, name, balance)
        self.minim_balance = minim_balance

    def withdrawal(self, money_to_withdrawal):
        if money_to_withdrawal <= self.balance - self.minim_balance:
            self.balance -= money_to_withdrawal
            print('Ati retras cu succes suma de ' + str(money_to_withdrawal) + '. Suma totala actuala: ' + str(
                self.balance))
        else:
            print('Tranzactie esuata.')

acc = Account("UOB2377",'Alexandra Dumitru', 380)
sacc = SavingsAccount("UOB4359",'Pavel Argat', 300, 0.75)
chacc = CheckingAccount("UOB0029",'Mika Thao', 7680, 250)

acc.deposit(1000)
sacc.interest_calculation()
chacc.withdrawal(2500)

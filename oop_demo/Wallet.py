
class Wallet:

    def __init__(self,name,initial_money):
        self.owner_name = name
        self.initial_money = initial_money

    def put_money(self,moneytoadd):
        self.initial_money += moneytoadd

    def withdraw_money(self,moneytoget):
        withdraw_value = 0
        if moneytoget <= self.initial_money:
            withdraw_value = moneytoget
            self.initial_money -= moneytoget
            return withdraw_value
        else:
            print("Your money is not enough!")

    def get_balance(self):
        return self.initial_money
from account import Account

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin, balance=0):
        self.accounts[account_number] = Account(account_number, pin, balance)

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, user_name, initial_deposit):
        user = User(user_name, initial_deposit)
        self.users.append(user)
        self.total_balance += initial_deposit
        print('Account created successfully.')

    def get_user(self, user_name):
        for user in self.users:
            if user.name == user_name:
                return user
        return None

    def check_total_balance(self):
        print('Total Available Balance:', self.total_balance)

    def check_total_loan_amount(self):
        print('Total Loan Amount:', self.total_loan_amount)

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        if self.loan_feature_enabled:
            print('Loan feature is now enabled.')
        else:
            print('Loan feature is now disabled.')


class User:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposit: {amount}')
        print('Amount deposited successfully.')

    def withdraw(self, amount, bank):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal: {amount}')
            print('Amount withdrawn successfully.')
        else:
            if bank.total_balance < amount:
                print('The Bank is Bankrupt')
            else:
                print('Insufficient balance.')

    def check_balance(self):
        print('Available Balance:', self.balance)

    def transfer(self, amount, recipient, bank):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f'Transfer: {amount} to {recipient.name}')
            recipient.transaction_history.append(f'Transfer: {amount} from {self.name}')
            print('Amount transferred successfully.')
        else:
            print('Insufficient balance.')

    def take_loan(self, bank):
        if not bank.loan_feature_enabled:
            print('Loan feature is currently disabled.')
            return

        loan_amount = self.balance * 2
        self.balance += loan_amount
        bank.total_loan_amount += loan_amount
        self.transaction_history.append(f'Loan: {loan_amount}')
        print('Loan taken successfully.')


bank = Bank()

bank.create_account('Sakib Khan', 1000)
bank.create_account('Jayed Khan', 500)

Sakib_Khan = bank.get_user('Sakib Khan')
Sakib_Khan.deposit(200)
Sakib_Khan.withdraw(300, bank)
Sakib_Khan.deposit(2000)
Sakib_Khan.withdraw(3000, bank)
Sakib_Khan.transfer(200, bank.get_user('Jayed Khan'), bank)
Sakib_Khan.check_balance()
Sakib_Khan.take_loan(bank)

Jayed_Khan = bank.get_user('Jayed Khan')
Jayed_Khan.check_balance()

bank.check_total_balance()
bank.check_total_loan_amount()
bank.toggle_loan_feature()
bank.toggle_loan_feature()
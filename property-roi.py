
class Income():
    def __init__(self, rent_inc, misc_inc = 0):
        self.rent_inc = rent_inc
        self.misc_inc = misc_inc
        self.total_inc = rent_inc + misc_inc

    def getIncome(self):
        return self.total_inc
    
class Expenses():
    def __init__(self, tax, insurance, util, mortgage, repairs, misc_exp = 0):
        self.tax = tax
        self.insurnace = insurance
        self.util = util
        self.mortgage = mortgage
        self.repairs = repairs
        self.misc_exp = misc_exp
        self.total_exp = tax + insurance + util + mortgage + repairs + misc_exp

    def getExpenses(self):
        return self.total_exp

class CalculateROI():
    def __init__(self, down_payment, closing, rehab_cost, income, expenses, misc_invest = 0):
        self.down_payment = down_payment
        self.closing = closing
        self.rehab_cost = rehab_cost
        self.income = income
        self.expenses = expenses
        self.misc_invest = misc_invest
        self.total_invest = down_payment + closing + rehab_cost + misc_invest

    def cashFlow(self):
        monthCashFlow = self.income - self.expenses
        yearlyCashFlow = monthCashFlow * 12
        return yearlyCashFlow

    def calcROI(self):
        return_on_investment = self.cashFlow() / self.total_invest
        return return_on_investment
        

def run():
    user_income = 0
    user_expenses = 0
    while True:
        print("\nWelcome to the Rental Property ROI Calculator.")
        choice = input("What would you like to do? \nType 'Income', to enter in income values, " +
            "\n'Expenses', to enter various expenses, or \n'Calculate' to calculate the ROI of your property. (if income and expenses are already known) " +
            "\nType 'Quit' to exit the program. ").lower()
        if choice == 'quit':
            break
        elif choice == 'income':
            print("\nPlease enter all values as numbers. Please enter '0' if the question does not apply.")
            rent_inc = int(input('What is the rental income of the property? '))
            misc_inc = int(input("Is there any other miscellanous income you would like to add? (ex. laundry, storage, etc.) "))
            user_income = Income(rent_inc, misc_inc).getIncome()
            print(f"Your total income is: {user_income}")
        elif choice == 'expenses':
            print("\nPlease enter all values as numbers. Please enter '0' if the question does not apply.")
            tax = int(input("What is the expected tax on the rental property? "))
            insurance = int(input("What is the expected insurance on the rental property? "))
            util = int(input("What are the expected utilities on the rental property? "))
            mortgage = int(input("What is the expected mortgage on the rental property? "))
            repairs = int(input("Are there any repair costs for the rental property? "))
            misc_exp = int(input("Are there any other miscellanous expenses for the rental property? "))
            user_expenses = Expenses(tax, insurance, util, mortgage, repairs, misc_exp).getExpenses()
            print(f"Your total expenses are: {user_expenses}")
        elif choice == 'calculate':
            print("\nPlease enter all values as numbers. Please enter '0' if the question does not apply.")
            down_payment = int(input("What is the down payment for the rental property? "))
            closing = int(input("What is the closing cost for the rental property? "))
            rehab_cost = int(input("What are any rehab costs for the rental property? "))
            misc_invest = int(input("Are there are any other miscellanous investments for the rental property? "))
            if not user_income:
                user_income = int(input("What is the total income for the property? "))
            if not user_expenses:
                user_expenses = int(input("What are the total expenses for the property? "))
            user_ROI = CalculateROI(down_payment, closing, rehab_cost, user_income, user_expenses, misc_invest).calcROI()
            print(f"Your cash on cash return on investment for this rental property is: {user_ROI*100}%")

run()

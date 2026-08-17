class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        somme = 0
        for charges in self.ledger:
            somme += charges['amount']
        return somme

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def transfer(self, amount, tocategory):
        if self.withdraw(amount, f'Transfer to {tocategory.name}'):
            tocategory.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def __str__(self):
        l3ibat = (30 - len(self.name))
        result = '*' * (l3ibat // 2) + f'{self.name}' + '*' * (l3ibat // 2 + l3ibat % 2) + '\n'
        for charges in self.ledger:
            result += f"{charges['description'][:23]}" + " " * ((23 - len(f"{charges['description'][:23]}")) + (
                        7 - len(f"{charges['amount']:.2f}"[:7]))) + f"{charges['amount']:.2f}\n"
        return result + 'Total: ' + f'{self.get_balance():.2f}'


def create_spend_chart(categories):
    result = "Percentage spent by category\n"

    # Calculate spending for each category
    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages rounded down to nearest 10
    percentages = []
    for amount in spent:
        percentages.append(int((amount / total_spent) * 10) * 10)

    # Draw the bars
    for level in range(100, -1, -10):
        result += f"{level:>3}|"
        for percent in percentages:
            if percent >= level:
                result += " o "
            else:
                result += "   "
        result += " \n"

    # Horizontal line
    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)
s
    for i in range(max_len):
        result += "     "
        for name in names:
            if i < len(name):
                result += name[i] + "  "
            else:
                result += "   "
        if i != max_len - 1:
            result += "\n"

    return result
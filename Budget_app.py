import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger= []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            amount = -amount
            self.ledger.append({'amount': amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total = total + entry['amount']
        return total

    def transfer(self, amount, other_category):
        if self.withdraw(amount, "Transfer to " + other_category.name):
            other_category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30, '*')
        lines = []
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amt = f"{entry['amount']:>7.2f}"
            lines.append(desc + amt)
        total = "Total: " + f"{self.get_balance():.2f}" 
        lines.insert(0, title)
        lines.append(total)
        return "\n".join(lines)

def create_spend_chart(categories):
    title = "Percentage spent by category"
    spent = []
    for category in categories:
        total = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                total = total + entry['amount']
        total = -total
        spent.append(total)
    total_spent = sum(spent)

    percentages = []
    for value in spent:
        percent = value / total_spent * 100
        percent = round(percent, 2)
        percent = percent / 10
        percent = math.floor(percent)
        percent = percent * 10
        percentages.append(percent)

    chart_lines = [title]
    for i in range(100, -10, -10):
        row = f"{i:>3}" + "|"
        for percent in percentages:
            if percent >= i:
                row += " o "
            else:
                row += "   "
        row += " "                       # <-- was "  ", now just 1 space
        chart_lines.append(row)

    # horizontal line
    line_length = 3 * len(categories) + 1   # <-- was +2, now +1
    chart_lines.append("    " + "-" * line_length)

    # vertical category name labels
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        label_row = "    "
        for category in categories:
            if i < len(category.name):
                letter = category.name[i]
            else:
                letter = " "
            label_row += " " + letter + " "
        label_row += " "                  # <-- was "  ", now just 1 space
        chart_lines.append(label_row)

    return "\n".join(chart_lines)



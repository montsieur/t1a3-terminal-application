"""

Expense module defining attributes used in expense tracker

"""
# Class for expense object(s)
class Expense:
    """

    This is the class that stores our expense information/attributes.

    """
    def __init__(self, name, date, amount, category, payment_method, budget=None) -> None:
        self.name = name
        self.date = date
        self.category = category
        self.amount = amount
        self.payment_method = payment_method
        self.budget = budget
class Expense:
    """

    This is the class that stores our expense information/attributes.

    """
    def __init__(self, name, date, category, amount, payment_method) -> None:
        self.name = name
        self.date = date
        self.category = category
        self.amount = amount
        self.payment_method = payment_method

# Encapsulation is bundaling of data and methods that operates on data into a single class.
# It is used to hide the implementation details from the user and provide a way to access the data.
# We use a double underscore prefix (__) to make attributes or methods private.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number      # Public
        self.__balance = balance                  # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid amount."

    def __hidden_method(self):
        return "This is a private method."

# Accessing members
account = BankAccount("12345", 1000)
print(account.deposit(500))         # Output: Deposited 500. New balance: 1500
# print(account.__balance)          # Raises AttributeError as it is private

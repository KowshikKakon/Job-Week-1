# self → wallet1

# other → wallet2


class Wallet():
    def __init__(self, owner,balance):
        self.balance = balance
        self.owner= owner

    def __add__(self, other):
        return Wallet(self.owner+other.owner, self.balance + other.balance)
wallet1 = Wallet("Alice", 500)
wallet2 = Wallet("Bob", 300)

wallet3 = wallet1 + wallet2

print(wallet3.balance)
print(wallet3.owner)

# I have used Self.owner and other.owner to concatenate the names of the wallet owners when adding two Wallet objects together.Just for fun...
#Task 10
'''Here our client wants us to make a program that can read data from a given tuple and convert it into
useful information to be used by the bank and the user. The tuple acts as a credit card'''
credit_card = ("Ali Raza",50000,20000,"Model town A")

name,card_balance,bank_balance,address = credit_card

print(f'''Account info is as follows:
Name: {name}
Card Balance: {card_balance}
Bank Balance: {bank_balance}
Address: {address}''')
# write a function named after transaction that returns the amount of money
# in the account after the transaction. If the transaction is negative and would
# overdraw the account, then the transaction should be ignored and the original 
# balance returned


def after_transaction(balance, transaction):
    total = balance + transaction
    if total >= 0: print(total)
    else: print(balance)

after_transaction(500,20)
after_transaction(300,-200)
after_transaction(3,-1000)
after_transaction(3,-4)
after_transaction(3,-3)
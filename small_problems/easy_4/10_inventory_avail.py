### Problem
# input: 1) id number, 2) transactions list
# output: boolean based on whether sum of "quantities" for each
# inventory item is 0 or more. 

### Data Structures
# list, containing dictionaries, each representing a transaction
# ints- id numbers and quantities
# strings- "out" and "in" representing adding or subtracting
# bools- our output

### Algorithm
# 1) Use prev function to get list of just the transactions for a 
# given id number
# 2) Loop through the list. For each transaction, determine:
# the quantity, and whether it was being added or subtracted (pos or neg)
# 3) Sum up your new list (of quantities, pos & neg) and return True if
# that total is greater than zero

def transactions_for(id_num, transactions_dict):
    return [trans_subdict 
            for trans_subdict in transactions_dict 
            if trans_subdict['id'] == id_num
    ]

def is_item_available(id_num, transactions_dict):
    this_item_transactions = transactions_for(id_num, transactions_dict)
    quantity_total = 0
    for transaction in this_item_transactions:
        if transaction['movement'] == 'in':
            quantity_total += transaction['quantity']
        else:
            quantity_total -= transaction['quantity']
    return quantity_total > 0


# Test cases
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
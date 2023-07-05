import numpy as np


data = {
    'products': [
        'bread eggs',
        'bread eggs milk',
        'milk cheese',
        'bread butter cheese',
        'eggs milk',
        'bread milk butter cheese',
    ]
}

sales = [transaction.split() for transaction in data['products']]
max_len = max(len(x) for x in sales)

arr = np.full((len(sales), max_len), np.nan, dtype='<U32')

for idx_trs, transaction in enumerate(sales):
    for idx_prod, product in enumerate(transaction):
        arr[idx_trs, idx_prod] = product

print(arr)
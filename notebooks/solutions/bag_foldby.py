import json

import dask.bag as db


bag = db.read_text(os.path.join('..', 'data', 'accounts.*.json.gz'))
js = bag.map(json.loads)


def sum_amount(total, user):
    transactions = user['transactions']
    return total + sum(transaction['amount'] for transaction in transactions)


js.foldby(key='name',
          binop=sum_amount,
          initial=0,
          combine=lambda x, y: x + y,
          combine_initial=0).compute()

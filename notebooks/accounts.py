import os

import numpy as np
import pandas as pd

names = ['Alice', 'Bob', 'Charlie', 'Dan', 'Edith', 'Frank', 'George',
         'Hannah', 'Ingrid', 'Jerry', 'Kevin', 'Laura', 'Michael', 'Norbert',
         'Oliver', 'Patricia', 'Quinn', 'Ray', 'Sarah', 'Tim', 'Ursula',
         'Victor', 'Wendy', 'Xavier', 'Yvonne', 'Zelda']

k = 100


def create_accounts_json(num_files, n, k):
    import json
    import gzip
    fn = os.path.join('data', 'accounts.%02d.json.gz' % (num_files - 1))
    if os.path.exists(fn):
        return

    print("Create JSON accounts for bag exercise")

    args = account_params(k)

    for i in range(num_files):
        seq = json_entries(n, *args)
        fn = os.path.join('..', 'data', 'accounts.%02d.json.gz' % i)
        with gzip.open(fn, 'wb') as f:
            f.write(os.linesep.join(map(json.dumps, seq)).encode())


def account_params(k):
    ids = np.arange(k, dtype=int)
    names2 = np.random.choice(names, size=k, replace=True)
    wealth_mag = np.random.exponential(100, size=k)
    wealth_trend = np.random.normal(10, 10, size=k)
    freq = np.random.exponential(size=k)
    freq /= freq.sum()

    return ids, names2, wealth_mag, wealth_trend, freq


def account_entries(n, ids, names, wealth_mag, wealth_trend, freq):
    indices = np.random.choice(ids, size=n, replace=True, p=freq)
    amounts = ((np.random.normal(size=n) + wealth_trend[indices])
                                         * wealth_mag[indices])

    return pd.DataFrame({'id': indices,
                         'names': names[indices],
                         'amount': amounts.astype('i4')},
                         columns=['id', 'names', 'amount'])


def accounts(n, k):
    ids, names, wealth_mag, wealth_trend, freq = account_params(k)
    df = account_entries(n, ids, names, wealth_mag, wealth_trend, freq)
    return df


def json_entries(n, *args):
    df = account_entries(n, *args)
    g = df.groupby(df.id).groups

    data = []
    for k in g:
        sub = df.iloc[g[k]]
        d = dict(id=int(k), name=sub['names'].iloc[0],
                transactions=[{'transaction-id': int(i), 'amount': int(a)}
                              for i, a in list(zip(sub.index, sub.amount))])
        data.append(d)

    return data


def accounts_json(n, k):
    args = account_params(k)
    return json_entries(n, *args)

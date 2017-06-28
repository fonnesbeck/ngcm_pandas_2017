import json
import dask.bag as db

bag = db.read_text(os.path.join('..', 'data', 'accounts.*.json.gz'))

js = bag.map(json.loads)

# first 5 users named Alice
js.filter(lambda x: x['name'] == "Alice").take(5)


def count_transactions(d):
    return {'name': d['name'], 'count': len(d['transactions'])}


(js.filter(lambda record: record['name'] == 'Alice')
   .map(count_transactions)
   .pluck('count')
   .take(5))

# Сценарий для вывода и обновления базы данных shelve,
# созданной в предыдущем сценарии

import shelve
db = shelve.open('dbfile')
for key in db:
    print(key, '=>',db[key])

bob = db['bob']
bob['age'] += 1
db['bob'] = bob
db.close()
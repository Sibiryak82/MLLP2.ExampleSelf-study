# Сценарий для заполнения базы данных shelve объектами Python

rec1 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'job':['dev', 'mgr'],
        'age': 40.5}

rec2 = {'name': {'first': 'Bob', 'last': 'Jones'},
        'job': ['mgr'],
        'age': 35.0}

import shelve
db = shelve.open('dbfile')
db['bob'] = rec1
db['bob'] = rec2
db.close()



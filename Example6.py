# Проверка возвращения в предыдущее состояние вывода для набора сценариев.

import os
testscripts = [dict(script='test1.py', args=''),     # Или глобальный каталог
                                                     # сценариев и аргументы
               dict(script='test2.py', args='spam')]

for testcase in testscripts:
    commandline = '%(script)s %(args)s' % testcase
    output = os.popen(commandline).read()
    result = testcase['script'] + '.result'
    if not os.path.exists(result):
        open(result, 'w').write(output)
        print('Created:', result)
    else:
        priorresult = open(result).read()
        if output != priorresult:
            print('FAILED:', testcase['script'])
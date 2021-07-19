# Утилита для просмотра и обслуживания исходящих сообщений
# электронной почты

"""
Просмотр почтового ящика и извлечение только заголовков с возможностью
удалять без загрузки полного сообщения
"""

import poplib, getpass, sys

mailserver = 'your pop email server name here'                # pop.server.net
mailuser = 'your pop user name here'
mailpasswd = getpass.getpass('Password for %s?' % mailserver)

print('Connecting...')
server = poplib.POP3(mailserver)

try:
    print(server.getwelcome())
    msgCount, mboxSize = server.stat()
    print('There are', msgCount, 'mail messges, size ', mboxSize)
    msginfo = server.list()
    print(msginfo)
    for i in range(msgCount):
        msgnum = i+1
        msgsize = msginfo[1][i].split()[1]
        resp, hdrlines, octets = server.top(msgnum, 0)        # Извлечь только
                                                              # заголовки
        print('-'*80)
        print('[%d: octets=%d, size=%s]' % (msgnum, octets, msgsize))
        for line in hdrlines: print(line)

        if input('Print?') in ['y', 'Y']:
            for line in server.retr(msgnum) [1]: print(line)  # Извлечь полное
                                                              # сообщение
        if input('Delete?') in ['y', 'Y']:
            print('deleting')
            server.dele(msgnum)                               # Удалить сообщение на сервере
        else:
            print('skipping')

finally:
    server.quit()                                             # Обеспечить разблокировку почтового ящика
    input('Bye.')                                             # Оставить окно открытым в Windows



# Извлечение и открытие/воспроизведение файла по протоколу FTP

import webbrowser, sys
from ftplib import FTP                       # Инструменты FTP на основе сокетов
from getpass import getpass                  # Скрытый ввод пароля
if sys.version[0] == '2': input = raw_input  # Совместимость с Python 2.X

nonpassive = False                           # Использовать активный режим FTP для сервера?
filename = input('File?')                    # Загружаемый файл
dirname = input('Dir') or '.'                # Удаленный каталог
sitename = input('Site?')                    # Сайт FTP
user = input('User?')                        # Использовать () для анонимного доступа
if not user:
    userinfo = ()
else:
    from getpass import getpass              # Скрытый ввод пароля
    userinfo = (user, getpass('Paswd?'))

print('Connecting...')
connection = FTP(sitename)                   # Подключение к сайту FTP
connection.login(*userinfo)                  # По умолчанию анонимный вход
connection.cwd(dirname)                      # Передавать по 1 Кбайт за раз в локальный файл
if nonpassive:                               # Применить активный режим FTP, если сервер требует
    connection.set_pasv(False)

print('Downloading...')
localefile = open(filename, 'wb')            # Локальный файл для хранения
                                             # загруженных данных
connection.retrbinary('RETR' + filename, localefile.write, 1024)
connection.quit()
localefile.close()

print('Playing...')
webbrowser.open(filename)
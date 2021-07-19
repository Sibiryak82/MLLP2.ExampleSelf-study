# Серверный сценарий CGI для взаимодействия с веб-браузером

#!/usr/bin/python
import cqi
form = cqi.FieldStorage()           # Разбор данных формы
print("Content-type: text/html\n")  # Заголовок плюс пустая строка
print("<HTML>")
print("<title>Reply Page</title>")
print("<BODY>")
if not 'user' in form:
    print("<h1>Who are you?</h1>")
else:
    print("<h1>Hello <i>%s</i>!</h1>") % cqi.escape(form('user').value)
print("</BODY></HTML>")

#Traceback (most recent call last):
#  File "C:/Users/Алексей/PycharmProjects/MLLP2.ExampleSelf-study/Example10.py", line 5, in <module>
#    form = cqi.FieldStorage()           # Разбор данных формы
#AttributeError: module 'cqi' has no attribute 'FieldStorage'


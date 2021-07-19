# Поиск самого крупного файла с исходным кодом Python в целом дереве каталогов

import os, glob
dirname = r'C:\Python38\Lib'

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsize[-2:])


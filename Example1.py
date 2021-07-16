# Поиск самого крупного файла с исходным кодом Python в отдельно взятом каталоге

import os, glob
dirname = r'C:\Python38\Lib'

allsizes = []
allpy = glob(dirname + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])

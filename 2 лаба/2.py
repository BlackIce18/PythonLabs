"""
Напишите скрипт, позволяющий искать в заданной директории и в ее
подпапках файлы-дубликаты на основе сравнения контрольных сумм
(MD5). Файлы могут иметь одинаковое содержимое, но отличаться
именами. Скрипт должен вывести группы имен обнаруженных файлов дубликатов.
"""

import hashlib
import os
import collections

StartPath = "2"
folder = [file for file in os.walk(StartPath)]
checksums = []
filename = []

for address, dirs, files in folder:
     for file in files:
        with open(address+'\\'+file, 'r', encoding='utf-8') as f:
            content = f.read()
        checksum = hashlib.md5(content.encode('utf-8')).hexdigest()
        checksums.append(checksum)
        filename.append(file)

duplicateHash = [item for item, count in collections.Counter(checksums).items() if count > 1]
duplicateFileName = []
for i in range(0, len(checksums)):
    for j in range(0, len(duplicateHash)):
        if checksums[i] == duplicateHash[j]:
            duplicateFileName.append(filename[i])

print("Найдены одинаковые файлы:")
print(duplicateFileName)

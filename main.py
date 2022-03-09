import os
from exam2csv import convertFile

for file in os.listdir('./tex'):
    if not file.startswith('.'):
        convertFile(file)

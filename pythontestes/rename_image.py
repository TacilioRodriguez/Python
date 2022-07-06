
import os
path = r'C:\Users\tacilio.pereira\Documents\GitHub\Python\pythontestes\\'

qtd = os.listdir(path)
number_files = len(qtd)
cont = 0
while cont < number_files:
    for cont, file_name in enumerate(qtd):
        os.rename(os.path.join(path, file_name), os.path.join(path, ''.join([str(cont), '.jpg'])))
        cont += 1


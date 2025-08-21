import datetime 
import os 
import time 

now = datetime.datetime.now()

print('Now :', now)

# Значение переменной now


# Чтение содержимого файла (если нужно)
with open('log.txt', 'r') as file:
    data = file.readlines()

# Внесение изменений в данные
# Добавляем новую строку с "Starting: now"
data.append(f"Starting: {now}\n")

# Сохранение изменений в файл
with open('log.txt', 'w') as file:
    file.writelines(data)

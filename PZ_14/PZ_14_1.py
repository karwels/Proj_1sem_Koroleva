# В исходном текстовом файле (Dostoevsky.txt) найти все фамилии с инициалами
# (например, А. Ф. Куманиной и т.п.).
import re
with open('Dostoevsky.txt', encoding='utf-8')as file: # открываем файл
    i = file.read()# читаем файл
f = re.findall(r'[А-Я]\.\s+[А-Я]\.\s+[А-Я][а-я]+', i) # создаем регулярное выражение
print(f)
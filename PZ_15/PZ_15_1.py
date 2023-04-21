# Разработать БД «ЗАРПЛАТА», содержащую две таблицы Анкета и
# Больничные листы. Установить связь между таблицами. Заполнить
# таблицы произвольными данными (не менее 10 записей). Реализовать
# SQL-запросы на выборку, обновление, удаление данных из БД.
# Таблица "Анкета"
# id (INT, PK) - уникальный идентификатор сотрудника
# имя (VARCHAR)
# фамилия (VARCHAR)
# дата_рождения (DATE)
# пол (VARCHAR)
# дата_найма (DATE)
# должность (VARCHAR)
# отдел (VARCHAR)
# базовая_ставка (DECIMAL)
# Таблица "Больничные листы"
# id (INT, PK) - уникальный идентификатор больничного листа
# id_сотрудника (INT, FK) - идентификатор сотрудника, на которого выписан больничный
# лист
# дата_начала (DATE)
# дата_окончания (DATE)
# причина (VARCHAR)
# диагноз (VARCHAR)
# оплачен (BOOLEAN)
# В данной структуре таблица "Больничные листы" связана с таблицей "Анкета" через
# внешний ключ id_сотрудника. Это означает, что каждый больничный лист относится к
# определенному сотруднику из таблицы "Анкета".
import sqlite3 as sq
from data_salary import *

with sq.connect('salary.db') as con:
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS anketa(
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        surname VARCHAR,
        data_of_birth DATE,
        sex VARCHAR,
        hire_data DATE,
        post VARCHAR,
        departament VARCHAR,
        base_rate DECIMAL
        )""")

with sq.connect('salary.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sick_list(
        id INTEGER PRIMARY KEY,
        id_sotr INTEGER,
        start_date DATE,
        end_date DATE,
        reason VARCHAR,
        diagnosis VARCHAR,
        paid BOOLEAN,
        FOREIGN KEY (id_sotr) REFERENCES salary(id) ON DELETE CASCADE ON UPDATE CASCADE
        )""")
# with sq.connect('salary.db') as con:
#         cur = con.cursor()
#         cur.executemany("INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", info_anketa)
#         cur.executemany("INSERT INTO sick_list VALUES (?, ?, ?, ?, ?, ?, ?)", info_list)
#  SELECT
# 1 Вывести список всех сотрудников и их должностей
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, surname, post FROM anketa ")
#     result = cur.fetchall()
# print(result)

# 2. Вывести список всех сотрудников и их базовых ставок
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, surname, base_rate  FROM anketa ")
#     result = cur.fetchall()
# print(result)

# 3. Вывести список всех сотрудников, работающих в отделе "IT"
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, surname FROM anketa WHERE departament = 'IT'")
#     result = cur.fetchall()
# print(result)

# 4. Вывести список всех сотрудников, принятых на работу после 1 января 2022 года
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, surname FROM anketa WHERE hire_data > '2022-01-01'")
#     result = cur.fetchall()
# print(result)

# 5. Вывести список всех больничных листов, выписанных сотруднику с id = 42
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id, start_date, end_date, reason, diagnosis, paid FROM sick_list WHERE id_sotr = 42")
#     result = cur.fetchall()
# print(result)

# 6. Вывести список всех больничных листов, оплаченных компанией
# with sq.connect('salary.db') as con:
#      cur = con.cursor()
#      cur.execute("SELECT id, start_date, end_date, reason, diagnosis FROM sick_list WHERE paid = 1")
#      result = cur.fetchall()
# print(result)

# 7. Вывести список всех сотрудников, имеющих больничные листы на текущий месяц
# with sq.connect('salary.db') as con:
#      cur = con.cursor()
#      cur.execute("SELECT anketa.name, anketa.surname FROM anketa INNER JOIN sick_list ON "
#                 "anketa.id = sick_list.id_sotr WHERE strftime('%m', sick_list.start_date ) = strftime('%m', 'now')")
#      result = cur.fetchall()
# print(result)

# 8. Вывести среднюю базовую ставку всех сотрудников
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT AVG(base_rate) FROM anketa")
#     result = cur.fetchall()
# print(result)

# 9. Вывести список всех сотрудников, имеющих базовую ставку выше 100 000
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, surname FROM anketa WHERE base_rate > 100000")
#     result = cur.fetchall()
# print(result)

# 10. Вывести список всех сотрудников и общее количество дней, проведенных ими на
# # больничном
# with sq.connect('salary.db') as con:
#     cur.execute("SELECT anketa.name, anketa.surname, "
#                 "SUM(julianday(sick_list.end_date) - julianday(sick_list.start_date)) "
#                 "FROM anketa INNER JOIN sick_list ON anketa.id = sick_list.id_sotr "
#                 "GROUP BY anketa.name, anketa.surname")
#     result = cur.fetchall()
# print(result)

# 11. Вывести информацию о сотрудниках и их больничных листах за последний месяц
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                         "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                         "INNER JOIN sick_list ON anketa.id = sick_list.id_sotr WHERE "
#                         "sick_list.start_date >= DATE('now', '-1 month')")
#     result = cur.fetchall()
# print(result)

#12. Вывести среднюю продолжительность больничных листов сотрудников в каждом
#отделе
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT departament, AVG(julianday(end_date) - julianday(start_date) + 1) FROM anketa "
#                         "INNER JOIN sick_list ON anketa.id = sick_list.id_sotr GROUP BY departament")
#     result = cur.fetchall()
# print(result)

# 13. Вывести список сотрудников и информацию о последнем больничном листе,
# который они оформляли
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                 "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                 "INNER JOIN sick_list ON anketa.id = sick_list.id "
#                 "WHERE sick_list.start_date = (SELECT MAX(start_date) "
#                 "FROM sick_list WHERE sick_list.id = anketa.id)")
#     result = cur.fetchall()
# print(result)

#14. Вывести список сотрудников и информацию о первом больничном листе, который они оформляли
# with sq.connect('salary.db') as con:
#     cur.execute("SELECT anketa.name, anketa.surname, sick_list.start_date, sick_list.end_date, "
#                "sick_list.reason, sick_list.diagnosis, sick_list.paid FROM anketa "
#                "INNER JOIN sick_list ON anketa.id = sick_list.id "
#                "WHERE sick_list.start_date = (SELECT MIN(start_date) "
#                "FROM sick_list WHERE sick_list.id = anketa.id)")
#     result = cur.fetchall()
# print(result)

#15.Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году
# with sq.connect('salary.db') as con:
#     cur.execute("SELECT name, surname, SUM(julianday(end_date) - julianday(start_date)) AS summa  FROM anketa "
#                 "INNER JOIN sick_list ON anketa.id = sick_list.id_sotr "
#                 "WHERE strftime('%Y', start_date) = strftime('%Y', 'now') "
#                 "GROUP BY name, surname ORDER BY summa")
#     result = cur.fetchall()
# print(result)

# UPDATE
#1. Обновить базовую ставку сотрудника на определенной должности.
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE anketa SET base_rate = 80000 WHERE post = 'Хирург'")
# 2. Обновить отдел для всех сотрудников в определенном диапазоне возраста.
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE anketa SET departament = 'Логистика' WHERE  data_of_birth BETWEEN '1990-01-01' AND '2000-01-01'")
# 3. Обновить дату найма для сотрудника, получившего повышение
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
    # добавила колонку "повышения"
    # cur.execute(" ALTER TABLE anketa ADD raising boolean ")
    # cur.execute(" UPDATE anketa SET raising = 0 WHERE id=42") #заполняла столбец raising
    # cur.execute(" UPDATE anketa SET hire_data = '2023-04-08' WHERE raising= 1 ")
# 4. Обновить причину больничного листа для сотрудника.
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute(" UPDATE sick_list SET reason = 'Болезнь' WHERE id_sotr = 7 ")
# 5. Обновить базовую ставку сотрудника в таблице "Анкета" на определенный
# процент, используя INNER JOIN с таблицей "Больничные листы". При этом
# необходимо исключить из обновления сотрудников, у которых были неоплаченные
# больничные листы.
#     cur.execute("UPDATE anketa SET base_rate = base_rate * 1.5 "
#                 "WHERE id IN(SELECT id_sotr FROM sick_list WHERE paid = 1)")
# 6. Обновить дату начала больничного листа в таблице "Больничные листы" на
# определенную дату, используя INNER JOIN с таблицей "Анкета". При этом
# необходимо исключить из обновления больничные листы с уже пройденной датой
# начала
#     cur.execute("UPDATE sick_list SET start_date = '2005-03-13' "
#                 "WHERE start_date < '2020-01-01'")
# 7. Обновить причину больничного листа в таблице "Больничные листы" на
# определенное значение для всех сотрудников, работающих в отделе "Бухгалтерия".
# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE sick_list SET reason = 'Авария' WHERE id_sotr "
#                       "IN (SELECT id FROM anketa WHERE departament = 'Бухгалтерия')")

# DELETE
# 1. Удалить все записи о больничных листах для сотрудника с именем "Иван"
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id FROM anketa WHERE name = 'Иван')")
# 2. Удалить все записи о больничных листах для сотрудника с фамилией "Петров"
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id FROM anketa WHERE surname = 'Петров')")
# 3. Удалить все записи о больничных листах для сотрудника с должностью
# "Менеджер"
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id FROM anketa WHERE post = 'Менеджер')")
# 4. Удалить все записи о больничных листах для сотрудника с отделом "Отдел
# продаж"
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("INSERT INTO sick_list values (1,1,'2022-04-01', '2022-04-14', 'Обморожение', 'Ангина', 1)")
#     cur.execute("INSERT INTO sick_list values (2,42,'2023-02-01', '2023-03-01', 'Яд', 'Отравление', 0)")
#     cur.execute("INSERT INTO sick_list values (3,2,'2010-08-09', '2010-08-30', 'Травма', 'Перелом ноги', 0)")
#     cur.execute("INSERT INTO sick_list values (4,3,'2022-01-02', '2022-01-16', 'Вирус', 'Коронавирус', 1)")
#     cur.execute("INSERT INTO sick_list values (5,4,'2019-03-02', '2019-03-16', 'Травма', 'Сотреение мозга', 1)")
#     cur.execute("INSERT INTO sick_list values (6,42,'2020-12-01', '2020-12-14', 'Обморожение', 'Ангина', 1)")
#     cur.execute("INSERT INTO sick_list values  (7,5,'2022-04-01', '2022-04-14', 'Укус змеи', 'Отек Квинке', 0)")
#     cur.execute("INSERT INTO sick_list values (8,6,'2022-09-26', '2022-10-5', 'Врожденная', 'Гимертония', 0)")
#     cur.execute("INSERT INTO sick_list values (9,7,'2010-07-07', '2010-07-25', 'Ожирение', 'Инсульт', 0)")
#     cur.execute("INSERT INTO sick_list values (10,9,'2017-05-07', '2017-05-28', 'Болезнь', 'Мигрень', 1)")
#     cur.execute("INSERT INTO sick_list values (11,10,'2013-01-03', '2013-03-28', 'Травма', 'Перелом', 1)")
#     cur.execute("INSERT INTO sick_list values (12,8,'2026-01-08', '2026-03-28', 'Травма', 'Перелом', 1)")
#     cur.execute("INSERT INTO sick_list values (13, 1,'2024-12-08', '2025-01-10', 'Вирус', 'Коронавирус', 0)")
#     cur.execute("INSERT INTO sick_list values (14,42,'2025-09-30', '2025-12-01', 'Обморожение', 'Ангина', 1)")
#     cur.execute("INSERT INTO sick_list values (15,3,'2026-02-28', '2026-03-28', 'Авария', 'Сотрясение мозга', 1)")
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id FROM anketa WHERE departament = 'Отдел продаж')")
# 5. Удалить все записи о больничных листах для сотрудника женского пола
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN(SELECT id FROM anketa WHERE sex = 'ж')")
# 6. Удалить все записи о больничных листах для сотрудников старше 50 лет
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id FROM anketa WHERE data_of_birth < '1973-01-01')")
# 7. Удалить все записи о неоплаченных больничных листах
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE paid = 0")
# 8. Удалить все записи о больничных листах, дата окончания которых прошла
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE end_date < DATE('now')")
# 9. Удалить все записи о больничных листах, начиная с определенной даты
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE start_date >= DATE('2026-01-01')")
# 10. Удалить все записи о больничных листах, закончившихся до определенной даты
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE end_date <= DATE('2025-09-30')")
# 11. Удалить все больничные листы сотрудника с именем "Иван" из таблицы
# "Больничные листы"
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
    # cur.execute("INSERT INTO sick_list values (1,1,'2022-04-01', '2022-04-14', 'Обморожение', 'Ангина', 1)")
    # cur.execute("INSERT INTO sick_list values (2,42,'2023-02-01', '2023-03-01', 'Яд', 'Отравление', 0)")
    # cur.execute("INSERT INTO sick_list values (3,2,'2010-08-09', '2010-08-30', 'Травма', 'Перелом ноги', 0)")
    # cur.execute("INSERT INTO sick_list values (4,3,'2022-01-02', '2022-01-16', 'Вирус', 'Коронавирус', 1)")
    # cur.execute("INSERT INTO sick_list values (5,4,'2019-03-02', '2019-03-16', 'Травма', 'Сотреение мозга', 1)")
    # cur.execute("INSERT INTO sick_list values (6,42,'2020-12-01', '2020-12-14', 'Обморожение', 'Ангина', 1)")
    # cur.execute("INSERT INTO sick_list values  (7,5,'2022-04-01', '2022-04-14', 'Укус змеи', 'Отек Квинке', 0)")
    # cur.execute("INSERT INTO sick_list values (8,6,'2022-09-26', '2022-10-5', 'Врожденная', 'Гимертония', 0)")
    # cur.execute("INSERT INTO sick_list values (9,7,'2010-07-07', '2010-07-25', 'Ожирение', 'Инсульт', 0)")
    # cur.execute("INSERT INTO sick_list values (10,9,'2017-05-07', '2017-05-28', 'Болезнь', 'Мигрень', 1)")
    # cur.execute("INSERT INTO sick_list values (11,10,'2013-01-03', '2013-03-28', 'Травма', 'Перелом', 1)")
    # cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id FROM anketa WHERE name='Иван')")
# 12. Удалить все больничные листы сотрудников, чьи фамилии начинаются на букву
# "С" из таблицы "Больничные листы"
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id FROM anketa WHERE surname LIKE 'С%')")
# 13. Удалить все больничные листы, которые еще не были оплачены, у сотрудников с
# должностью "Менеджер" из таблицы "Больничные листы"
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
    # cur.execute("INSERT INTO sick_list values (1,1,'2022-04-01', '2022-04-14', 'Обморожение', 'Ангина', 0)")
    # cur.execute(" DELETE FROM sick_list WHERE paid=0 AND id_sotr "
    #             "IN (SELECT id FROM anketa WHERE post='Менеджер')")
# 14. Удалить все больничные листы, выписанные сотрудникам отдела "IT" в период с 1
# января
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("INSERT INTO sick_list values (34, 5,'2023-05-07', '2023-05-28', 'Болезнь', 'Мигрень', 1)")
#     cur.execute("INSERT INTO sick_list values (35, 2,'2023-01-03', '2023-03-28', 'Травма', 'Перелом', 0)")
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id FROM anketa WHERE departament='IT') "
#                 "AND start_date >= '2023-01-01'")
# 15. Удалить все больничные листы, связанные со сотрудниками старше 50 лет из
# таблицы "Больничные листы"
# with sq.connect("salary.db") as con:
#     cur = con.cursor()
#     cur.execute("INSERT INTO sick_list values (6,42,'2020-12-01', '2020-12-14', 'Обморожение', 'Ангина', 1)")
#     cur.execute("DELETE FROM sick_list WHERE id_sotr IN (SELECT id FROM anketa WHERE data_of_birth <= '1973-01-01')")






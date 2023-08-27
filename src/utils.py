import psycopg2
import requests
from config import config
from typing import Any

database_name = 'database_hh'

def get_hh_data(employer_id):
    """получает данные с hh.ru по API, принимает номер компании"""
    employers_ids = [1122462, 9498120, 3776, 3529, 78638]
    #[Skyeng, Yandex, МТС, Сбер, Тинькофф]
    #https://api.hh.ru/vacancies?employer_id=78638&per_page=5
    #url = "https://api.hh.ru/vacancies/"
    #list_of_vacancies = []
    for _id in employers_ids:
        params = {'employer_id: _id,'
                  'per_page': 20}
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    data = response.json()['items']
    #list_of_vacancies.append(data)
    return data

def get_vacancy_info():
    vacancies = []
    for item in data:
            dict =
            {   'vacancy_name': item["name"],  # название вакансии
                'vacancy_url': item['alternate_url'], #ссылка на вакансию
                'vacancy_id': item["id"],
                'salary': item["salary"]  # зарплата
                if salary:
                    salary = item["salary"]["from"]
                    if not salary:
                        salary = 0
                    else:c
                        salary = 0
                'employer_id': item['employer']['id'],
                'employer_name': item['employer']['name'],
            }
    vacancies.append(dict)
    return vacancies

# def create_database(database_name: str, params: dict):
#     """Создание базы данных и таблиц для сохранения данных о работодателях и вакансиях"""
#
#     conn = psycopg2.connect(dbname='postgres', **params)
#     conn.autocommit = True
#     cur = conn.cursor()
#
#     cur.execute(f"DROP DATABASE {database_name}")
#     cur.execute(f"CREATE DATABASE {database_name}")
#
#     conn.close()
#
#     conn = psycopg2.connect(dbname=database_name, **params)
#
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE employers (
#                 employer_id INT  PRIMARY KEY,
#                 employer_name VARCHAR(100) NOT NULL,
#                 city VARCHAR(100) NOT NULL,
#                 site_url TEXT,
#                 description TEXT
#             );
#         """)
#
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE vacancies (
#                 vacancy_name VARCHAR(100) NOT NULL,
#                 vacancy_id INT PRIMARY KEY,
#                 vacancy_url TEXT,
#                 employer_id INT REFERENCES employers(employer_id),
#                 salary_from INTEGER,
#                 salary_to INTEGER,
#
#             );
#         """)
#
#     conn.commit()
#     conn.close()
#
# def save_data_to_database(data: list[dict[str, Any]], database_name:str, params: dict):
#     """наполнение таблиц данными"""
# #    with (psycopg2.connect(host="localhost", database="north", user="postgres", password="541709") as conn):
#     conn = psycopg2.connect(dbname=database_name, **params)
#         with conn.cursor() as cur:
#             # with open("north_data/employees_data.csv", "r", encoding="UTF-8") as file:
#             #     file_reader = csv.reader(file, delimiter=",")
#             #     count = 0
#             #     for row in file_reader:
#             #         if count == 0:
#             #             count += 1
#             #             continue
#             for vacancy in data:
#                 cur.execute("INSERT INTO vacancies values (%s, %s, %s, %s, %s, %s)",
#                                 (row[0], row[1], row[2], row[3], row[4], row[5]))
#
#                 cur.execute("SELECT * FROM vacancies")
#                 rows = cur.fetchall()
#                 for row in rows:
#                     print(rows)
#
#
#         with conn.cursor() as cur:
#             for employer in data:
#                 cur.execute("INSERT INTO employers values (%s, %s, %s, %s, %s)",
#                     (row[0], row[1], row[2], row[3], row[4]))
#
#                 cur.execute("SELECT * FROM employers")
#                 rows = cur.fetchall()
#                 for row in rows:
#                     print(rows)
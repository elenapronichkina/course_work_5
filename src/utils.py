import os
import psycopg2
import requests

password = os.getenv('PASSWORD_PG')


def load_employers():
    employers_ids = [1122462, 9498120, 3776, 3529, 78638]
    conn = psycopg2.connect(dbname='database_hh', user='postgres', password=password, host='localhost', port=5432)
    cur = conn.cursor()

    for _id in employers_ids:
        data = requests.get(f'https://api.hh.ru/employers/{_id}').json()

        cur.execute("""
            INSERT INTO employers (employer_id, employer_name, city, site_url, description) VALUES
            (%s, %s, %s, %s, %s);""", (
            _id,
            data.get('name'),
            data.get('area').get('name'),
            data.get('site_url'),
            data.get('description')
        ))

    cur.close()
    conn.commit()
    conn.close()


def load_vacancies():
    employers_ids = [1122462, 9498120, 3776, 3529, 78638]

    conn = psycopg2.connect(dbname='database_hh', user='postgres', password=password, host='localhost', port=5432)
    cur = conn.cursor()

    for _id in employers_ids:

        data = requests.get(f'https://api.hh.ru/vacancies?employer_id={_id}&per_page=5').json()
        # print (data)
        for item in data["items"]:
            cur.execute("""
                INSERT INTO vacancies (vacancy_id, vacancy_name, vacancy_url, salary_from, salary_to,employer_id) VALUES
                (%s, %s, %s, %s, %s, %s);""", (
                item.get('id'),
                item.get('name'),
                item.get('alternate_url'),
                item.get('salary').get('from') if item.get('salary') else 0,
                item.get('salary').get('to') if item.get('salary') else 0,
                _id
            ))

    cur.close()
    conn.commit()
    conn.close()


def create_tables():
    """Создание таблиц для сохранения данных о работодателях и вакансиях"""

    conn = psycopg2.connect(dbname='database_hh', user='postgres', password=password, host='localhost', port=5432)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers (
                employer_id INT  PRIMARY KEY,
                employer_name VARCHAR(100) NOT NULL,
                city VARCHAR(100) NOT NULL,
                site_url TEXT,
                description TEXT
            );
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id INT PRIMARY KEY,
                vacancy_name VARCHAR(100) NOT NULL,
                vacancy_url TEXT,
                salary_from INTEGER DEFAULT 0,
                salary_to INTEGER DEFAULT 0,
                employer_id INT REFERENCES employers(employer_id)
            );
        """)

    conn.commit()
    conn.close()


def create_database(database_name):
    """Создание базы данных для сохранения данных о каналах и видео."""
    conn = psycopg2.connect(dbname='postgres', user='postgres', password=password, host='localhost', port=5432)
    cur = conn.cursor()

    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()


def drop_database(database_name):
    """Создание базы данных для сохранения данных о каналах и видео."""
    conn = psycopg2.connect(dbname='postgres', user='postgres', password=password, host='localhost', port=5432)
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")

    cur.close()
    conn.close()

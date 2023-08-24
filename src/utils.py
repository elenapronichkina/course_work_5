import psycopg2
from config import HOST, PORT, DATABASE, USER, PASSWORD
def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о работодателях и вакансиях"""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers (
                employer_id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                city VARCHAR(100) NOT NULL,
                site_url TEXT,
                description TEXT
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY,
                employer_id INT REFERENCES employers(employer_id),
                name VARCHAR(100) NOT NULL,
                salary INT,
                vacancy_url TEXT
            )
        """)

    conn.commit()
    conn.close()

def insert_data_to_tables():
    """наполнение таблиц данными"""
    with (psycopg2.connect(host="localhost", database="north", user="postgres", password="541709") as conn):
        with conn.cursor() as cur:
            with open("north_data/employees_data.csv", "r", encoding="UTF-8") as file:
                file_reader = csv.reader(file, delimiter=",")
                count = 0
                for row in file_reader:
                    if count == 0:
                        count += 1
                        continue
                    cur.execute("INSERT INTO employees values (%s, %s, %s, %s, %s, %s)",
                                (row[0], row[1], row[2], row[3], row[4], row[5]))

                cur.execute("SELECT * FROM employees")
                rows = cur.fetchall()
                for row in rows:
                    print(rows)

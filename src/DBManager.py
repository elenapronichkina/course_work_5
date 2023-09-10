import params
import psycopg2
#from src.utils import database_name
conn = psycopg2.connect(dbname='database_hh', user='postgres', password=541709, host='localhost', port=5432)
#conn = psycopg2.connect(dbname=database_name, **params)
class DBManager:
    """класс для работы с БД: подключается к БД PostgreSQL"""
    def __init__(self):
        self.conn = conn

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(vacancy_id),employer_name
                FROM vacancies
                INNER JOIN employers USING(employer_id)
                GROUP BY employers.employer_name
                """)
            rows = cur.fetchall()
            print(rows)
        conn.commit()

    def get_all_vacancies(self):
       """получает список всех вакансий с указанием названия компании,
       названия вакансии и зарплаты и ссылки на вакансию."""
       with conn.cursor() as cur:
           cur.execute("""
                SELECT employers.employer_name, vacancy_name, salary_from, salary_to, vacancy_url 
                FROM vacancies
                INNER JOIN employers USING(employer_id)
                    """)
           rows = cur.fetchall()
           print(rows)

       conn.commit()

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        with conn.cursor() as cur:
            cur.execute("""
                 SELECT vacancy_name, AVG(salary_from+salary_to)
                 FROM vacancies
                 GROUP BY vacancy_name
                    """)
            rows = cur.fetchall()
            print(rows)

        conn.commit()

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых
            зарплата выше средней по всем вакансиям."""
        with conn.cursor() as cur:
            cur.execute("""
                    SELECT *
                    FROM vacancies
                    WHERE salary_from > (SELECT AVG(salary_from+salary_to) FROM vacancies)
                        """)
            rows = cur.fetchall()
            print(rows)

        conn.commit()

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых
            содержатся переданные в метод слова"""
        user_word = str(input())
        word = user_word.casefold()
        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT *  
            FROM vacancies
            WHERE vacancy_name LIKE '{word}%' 
            OR vacancy_name LIKE '%{word}' 
            OR vacancy_name LIKE '%{word}%'
                """)
            rows = cur.fetchall()
            print(rows)

        conn.commit()

    def conn_close(self):
        self.conn.close()
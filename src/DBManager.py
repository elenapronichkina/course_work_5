import params
import psycopg2
from config import config
from src.utils import database_name

conn = psycopg2.connect(dbname=database_name, **params)
class DBManager:
    """класс для работы с БД: подключается к БД PostgreSQL"""
    def __init__(self, employer_id):
        self.employer_id = employer_id
        self.conn = psycopg2.conn()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        with conn.cursor() as cur:
            cur.execute("""
        SELECT DISTINCT employer_name 
        FROM employers
        INNER JOIN vacancies USING(employer_id);
        
        SELECT COUNT(vacancy_id) 
        FROM vacancies
        INNER JOIN employers USING(employer_id)
        """)
        conn.commit()
        conn.close()

    def get_all_vacancies(self):
       """получает список всех вакансий с указанием названия компании,
       названия вакансии и зарплаты и ссылки на вакансию."""
       with conn.cursor() as cur:
           cur.execute("""
                SELECT vacancy_name, salary, vacancy_url, employer_name
                FROM vacancies
                INNER JOIN employers(employer_id)

                """)
       conn.commit()
       conn.close()

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        with conn.cursor() as cur:
            cur.execute("""
                 SELECT AVG(salary)
                 FROM vacancies
                 """)
        conn.commit()
        conn.close()

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых
            зарплата выше средней по всем вакансиям."""
        word = str(input())
        with conn.cursor() as cur:
            cur.execute(f"""
                    SELECT (*)  
                    FROM vacancies
                    WHERE salary > AVG(salary)
                    """)

        conn.commit()
        conn.close()

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых
            содержатся переданные в метод слова"""
        word = str(input())
        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT (*)  
            FROM vacancies
            WHERE vacancy_name LIKE '% {word})';
            """)

        conn.commit()
        conn.close()
    def create_tables(self):
        pass

    def drop_tables(self):
        pass
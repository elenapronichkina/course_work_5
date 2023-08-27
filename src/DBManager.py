import psycopg2
class DBManager:
    """класс для работы с БД: подключается к БД PostgreSQL"""
    def __init__(self, employer_id):
        self.employer_id = employer_id
        self.conn = psycopg2.conn()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        with conn.cursor() as cur:
            cur.execute("""
        SELECT DISTINCT employer_name FROM employers
        INNER JOIN vacancies USING(employer_id)
        """)

    def get_all_vacancies(self):
       """получает список всех вакансий с указанием названия компании,
       названия вакансии и зарплаты и ссылки на вакансию."""
        pass

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        pass

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        pass

    def create_tables(self):
        pass

    def drop_tables(self):
        pass
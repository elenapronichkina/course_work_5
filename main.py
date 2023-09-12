from src.DBManager import DBManager
from src.utils import create_database, drop_database, create_tables, load_employers, load_vacancies


def main():
    employers_ids = [1122462, 9498120, 3776, 3529, 78638]
    """[Skyeng, Yandex, МТС, Сбер, Тинькофф]"""

    drop_database('database_hh')
    create_database('database_hh')
    create_tables()
    load_employers()
    load_vacancies()

    db = DBManager()
    print("Cписок компаний и количество вакансий у них:")
    print(db.get_companies_and_vacancies_count())
    print("Список всех вакансий с указанием названия компании:")
    print(db.get_all_vacancies())
    print("Средняя зарплата по вакансиям:")
    print(db.get_avg_salary())
    print("Вакансии с зарплатой выше средней по всем вакансиям:")
    print(db.get_vacancies_with_higher_salary())
    print("Введите наименование вакансии: ")
    print(db.get_vacancies_with_keyword())
    db.conn_close()


if __name__ == '__main__':
    main()

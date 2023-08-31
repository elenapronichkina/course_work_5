#from src.DBManager import DBManager
from src.utils import create_database, drop_database, create_tables, load_employers, load_vacancies

def main():
    employers_ids = [1122462, 9498120, 3776, 3529, 78638]
    """[Skyeng, Yandex, МТС, Сбер, Тинькофф]"""

    drop_database('database_hh')
    create_database('database_hh')
    create_tables()
    load_employers()
    load_vacancies()

    # db = DBManager()
    #
    # print(db.get_all_vacancies())
    # print(db.get_avg_salary())
    # print(db.get_vacancies_with_higher_salary())
    # print(db.get_vacancies_with_keyword())
    # print(db.get_vacancies_with_keyword())


if __name__ == '__main__':
    main()



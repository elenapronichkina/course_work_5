from src.DBManager import DBManager()
from src.utils import get_hh_data, create_database, save_data_to_database
from config import config

def main():
    employers_ids = [1122462, 9498120, 3776, 3529, 78638]
    """[Skyeng, Yandex, МТС, Сбер, Тинькофф]"""

    params = config()
    db = DBManager()
    db.connect
    # drop_tables
    # create_tables
    for employer_id in employers_ids:
        data = get_hh_data(employer_id)
        create_database('database_hh', params)
        save_data_to_database(data, 'database_hh', params)

print(db.get_all_vacancies())
print(db.get_avg_salary())
print(db.get_vacancies_with_higher_salary())
print(db.get_vacancies_with_keyword())
print(db.get_vacancies_with_keyword())


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

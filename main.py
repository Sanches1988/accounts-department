from application import salary
from application.db import people
from datetime import datetime as dt

if __name__ == '__main__':
    print(dt.now(tz=None))
    print(salary.calculate_salary(18, 35))
    print(people.get_employees())

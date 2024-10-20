"""Модуль для выполнения системных команд."""

import os

from datetime import datetime, timedelta


def make_commits(start_date: datetime, end_date: datetime):
    """Создание коммитов от start_date до end_date."""
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%d.%m.%Y г.')
        with open('data.txt', 'a', encoding='utf-8') as file:
            file.write(f'{date_str}\n')

        os.system('git add data.txt')
        os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

        current_date += timedelta(days=1)

    os.system('git push -u origin main')


def main():
    """Главная функция для задания диапазона дат и вызова функции коммитов."""
    start_date = datetime()
    end_date = datetime()
    make_commits(start_date, end_date)


if __name__ == '__main__':
    main()

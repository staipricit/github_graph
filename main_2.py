"""Модуль для выполнения системных команд."""

import os

from datetime import datetime


def make_commits(dates: list):
    """Создание коммитов от start_date до end_date."""
    for commit_date in dates:
        date_str = commit_date.strftime('%d.%m.%Y г.')
        with open('data.txt', 'a', encoding='utf-8') as file:
            file.write(f'{date_str}\n')

        os.system('git add data.txt')
        os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

    os.system('git push -u origin main')


def main():
    """Главная функция для задания диапазона дат и вызова функции коммитов."""
    commit_dates = [datetime()]

    make_commits(commit_dates)


if __name__ == '__main__':
    main()

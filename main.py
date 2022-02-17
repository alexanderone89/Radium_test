"""Модуль main."""
import asyncio
import hashlib
import random
import re
import sys

import requests
from bs4 import BeautifulSoup


def get_vacancy_salary(url):
    """Возвращает список извлеченных данных из url страницы.

    Args:
        url (str): ссылка на страницу вакансии

    Returns:
        vaca_sal (list): список [название вакансии, зарплата]
    """
    headers = {
        'Accept-Language': 'content-copied-from-myhttpheader',
        'User-Agent': 'content-copied-from-myhttpheader',
    }

    res = requests.get(url, headers=headers)
    vaca_sal = []
    if int(res.status_code) == int('200'):
        soup = BeautifulSoup(res.text, 'html.parser')
        vaca_sal.append(soup.find('h1', class_='bloko-header-1').text)
        t_salary = soup.find('span', class_='bloko-header-2').text
        vaca_sal.append(
            int(re.sub(r'[\s]+|[^\d]+', '', t_salary).strip()),
        )
    return vaca_sal


async def print_text(end_delay, text):
    """Функция вывода данных.

    Args:
        end_delay (int): задержка перед выводом текста
        text (str): текст (имя, название вакансии, ожидаемая зп через год)
    """
    rng = random.SystemRandom()
    delay = rng.randint(1, end_delay)
    await asyncio.sleep(delay)
    sys.stdout.write('Вывод {0} с задержкой {1} сек'.format(text, delay))


async def main():
    """Главная функция."""
    vac_sal = get_vacancy_salary(
        'https://hh.ru/vacancy/51992559',
    )
    timeout_sec = 5
    if vac_sal:
        await asyncio.gather(
            print_text(timeout_sec, 'Добрый день, меня зовут Александр'),
            print_text(timeout_sec, vac_sal[0]),
            print_text(timeout_sec, vac_sal[1]),
        )
    else:
        sys.stdout.write('Vacancy not found or no internet connection!\n')
        loop = asyncio.get_event_loop()
        loop.stop()


if __name__ == '__main__':
    asyncio.run(main())
    sys.stdout.write('Введите текст для шифрования :\n')
    str_input = sys.stdin.read()
    hash_str = hashlib.sha256(str_input.encode('utf-8')).hexdigest()
    sys.stdout.write(str(hash_str))

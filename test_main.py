"""Модуль теста main."""
import unittest

from main import get_vacancy_salary, print_text


class TestMain(unittest.TestCase):
    """Класс автотеста main."""

    def test_len_list(self):
        """Тест проверки выходного списка функции.

        get_vacancy_salary на заполненность
        """
        url = 'https://taganrog.hh.ru/vacancy/50927402'
        res = get_vacancy_salary(url)
        self.assertTrue(bool(res))

    def test_elmnt_isnone(self):
        """Тест проверки содержимого элементов списка функции.

        get_vacancy_salary на пустоту
        """
        url = 'https://taganrog.hh.ru/vacancy/50927402'
        res = get_vacancy_salary(url)
        self.assertIsNotNone(res[0])
        self.assertIsNotNone(res[1])

    def test_signint(self):
        """Проверка интервала на отрицательное целое число в print_text."""
        text = '111'
        interval = 5
        self.assertTrue(bool(interval > 0))
        print_text(interval, text)


if __name__ == '__main__':
    unittest.main()

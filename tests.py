import unittest
from flask import Flask, render_template, request
import math
from app import app, calculate_mortgage_payment  # Импортируем функции из app.py

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1 class="title">Mortgage Calculator</h1>', response.data)

    def test_form_route(self):
        response = self.app.post('/', data=dict(
            loan_amount='100000',
            interest_rate='5',
            loan_term='30'
        ))
        self.assertEqual(response.status_code, 200)
        # Проверяем, что в ответе есть рассчитанный платеж
        self.assertIn(b'Monthly payment: $536.82', response.data)  # Используем точный результат (округляем до 2 знаков после запятой)

    def test_calculate_mortgage_payment(self):
        # Проверяем функцию расчета ипотечного платежа
        monthly_payment = calculate_mortgage_payment(100000, 5, 30)
        self.assertAlmostEqual(monthly_payment, 536.82, 2)  # Проверка с точностью до 2 знаков после запятой

if __name__ == '__main__':
    unittest.main()
# Practical-work-13


# Задание
Реализовать финансовый калькулятор.

* Часть 1: Настройка проекта
  1. Создайте папку financial_calc и перейдите в неё

  2. Инициализируйте проект с помощью uv

  3. Установите pytest через uv

  4. Создайте файл calculator.py с функциями и папку tests с файлом test_calculator.py

* Часть 2: Реализация функций
В файле calculator.py создайте 3 функции:

  1. calculate_simple_interest(principal, rate, time)
     
    * Формула: principal * rate * time / 100

    * Возвращает: float

    * При отрицательных аргументах вызывает ValueError("Аргументы должны быть неотрицательными")

  2. calculate_compound_interest(principal, rate, time, n=1)

    * Формула: principal * (1 + rate/(100*n))**(n*time)

    * n должно быть целым положительным числом

    * При некорректных аргументах вызывает ValueError

  3. calculate_tax(amount, tax_rate)

    * Формула: amount * tax_rate / 100

    * Возвращает сумму налога

    * Если tax_rate не между 0 и 100, вызывает ValueError

Часть 3: Написание тестов
В файле tests/test_calculator.py напишите тесты:

Для каждой функции проверьте:

Правильность расчёта (минимум 2 примера)

Работу с нулевыми значениями

Вызов ValueError при отрицательных значениях

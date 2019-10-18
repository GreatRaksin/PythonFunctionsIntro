"""
Определяем функцию для подсчета суммы покупки с учетом налога
"""


def CalculateTax(price, TaxRate):
    """
    Внутри функции задаем два аргумента
    :param price:
    :param TaxRate:
    Добавляем переменную для подсчета суммы, а затем возвращаем ее значение
    :return:
    """
    TaxTotal = price + (price * TaxRate / 100)
    return TaxTotal


param1 = float(input('Введите сумму покупки в долларах: '))
param2 = float(input('Введите процентную ставку вашего штата: '))

print(f'Сумма покупки с учетом налога составит: ${CalculateTax(param1, param2)}')

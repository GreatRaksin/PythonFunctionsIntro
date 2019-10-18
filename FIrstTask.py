# coding=utf-8
"""
Для начала определим функцию с одним аргументом.
"""


def MyAddress(name):
    """
    Внутри тела функции будем выводить пользователю
    строчки с его именем и адресом
    """
    print(name)
    print("220080")
    print("Kiseleva st., 12, office 20.")
    print("Belarus, Minsk")

YourName = input('Как вас зовут?')

print(MyAddress(YourName))

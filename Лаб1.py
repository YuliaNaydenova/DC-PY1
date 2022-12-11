import doctest


class Employee:
    def __init__(self, position: str, salary: float):
        """
                Создание и подготовка к работе объекта "Работник"
                :param position: должность работника
                :param salary: зарплата работника
                Примеры:
                >>> employee1 = Employee('manager', 45000)  # инициализация экземпляра класса
                """
        self.position = position
        if not isinstance(salary, (int, float)):
            raise TypeError("Зарпалата должна быть типа int или float")
        if salary <= 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.salary = salary

    def salary_increase(self, increase: float) -> None:
        """
                Увеличение зарплаты
                :param increase: на сколько увеличиваем зарпату
                Примеры:
                >>> employee1 = Employee('salesman', 45000)
                >>> employee1.salary_increase(1000)
                """
        if not isinstance(increase, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if increase < 0:
            raise ValueError("Сумма должна быть положительным числом")
        ...

    def salary_decrease(self, decrease: float) -> None:
        """
                Уменьшение зарплаты
                :param decrease: на сколько уменьшаем зарпату
                :raise ValueError: Если сумма, на которую уменьшаем з/п, больше з/п, то вызываем ошибку
                Примеры:
                >>> employee1 = Employee('salesman', 45000)
                >>> employee1.salary_decrease(1000)
                """
        if not isinstance(decrease, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if decrease < 0:
            raise ValueError("Сумма должна положительным числом")
        ...

    def change_position(self, new_position) -> None:
        """
                Меняем должность сотрудника
                :param new_position: новая должность
                >>> employee1 = Employee('salesman', 45000)
                >>> employee1.change_position('manager')
                """


class Hairstyle:
    def __init__(self, color: str, length: float, type: str):
        """
                Создание и подготовка к работе объекта "Прическа"
                :param color: цвет волос
                :param length: длина волос
                :param type: тип волос
                Примеры:
                >>> hairstyle1 = Hairstyle('dark', 28.5, 'wavy')  # инициализация экземпляра класса
                """
        self.color = color
        self.type = type
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

    def is_long(self) -> bool:
        """
        Функция которая проверяет являются ли волосы длинными
        :return: Являются ли волосы длинными
        Примеры:
        >>> hairstyle = Hairstyle('dark', 28.5, 'wavy')
        >>> hairstyle.is_long()
        """
        ...

    def cut_hair(self, decrease: float) -> None:
        """
                Стрижем волосы
                :param decrease: на сколько укорачиваем волосы
                :raise ValueError: Если длина, на которую укорачиваем волосы, больше длины волос, то вызываем ошибку
                Примеры:
                >>> hairstyle = Hairstyle('dark', 28.5, 'wavy')
                >>> hairstyle.cut_hair(10)
                """
        if not isinstance(decrease, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if decrease < 0:
            raise ValueError("Длина должна положительным числом")
        ...

    def change_color(self, new_color) -> None:
        """
                Меняем цвет волос
                :param new_color: новый цвет
                >>> hairstyle = Hairstyle('brown', 28.5, 'wavy')
                >>> hairstyle.change_color('blonde')
                """


class Drink:
    def __init__(self, price: float, volume: float):
        """
                Создание и подготовка к работе объекта "Напиток"
                :param price Цена напитка
                :param volume Обьем напитка
                Примеры:
                >>> drink1 = Drink(60, 0.5)  # инициализация экземпляра класса
                """
        self.price = price
        self.volume = volume

    def price_increase(self, increase: float) -> None:
        """
                Увеличиваем цену
                :param increase: на сколько увеличиваем цену
                Примеры:
                >>> drink1 = Drink(60.0, 0.5)
                >>> drink1.price_increase(10.0)
                """
        if not isinstance(increase, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if increase < 0:
            raise ValueError("Сумма должна быть положительным числом")
        ...

    def price_decrease(self, decrease: float) -> None:
        """
                Уменьшаем цену
                :param decrease: на сколько уменьшаем цену
                :raise ValueError: Если сумма, на которую уменьшаем цену, больше цены, то вызываем ошибку
                Примеры:
                >>> drink1 = Drink(60, 0.5)
                >>> drink1.price_decrease(70)
                """
        if not isinstance(decrease, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if decrease < 0:
            raise ValueError("Сумма должна быть положительным числом")
        ...



if __name__ == "__main__":
    doctest.testmod()
import doctest

class Employee:
    def __init__(self, name: str, position: str, salary: float):
        """
                Создание и подготовка к работе объекта "Работник"
                :param name: имя работника
                :param position: должность работника
                :param salary: зарплата работника
                Примеры:
                >>> employee1 = Employee('Иван Иванов','manager', 45000)  # инициализация экземпляра класса
                """
        self.name = name
        self.position = position
        if not isinstance(salary, (int, float)):
            raise TypeError("Зарпалата должна быть типа int или float")
        if salary <= 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.salary = salary

    def __str__(self):
        return f"Работник {self.name}, {self.position} с з/п {self.wage}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, position={self.position!r})"

    def salary_increase(self, name, increase: float) -> None:
        """
                Увеличение зарплаты
                :param increase: на сколько увеличиваем зарпату
                Примеры:
                >>> employee1 = Employee('Иван Иванов', 'salesman', 45000)
                >>> employee1.salary_increase('Иван Иванов', 1000)
                """
        if not isinstance(increase, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if increase < 0:
            raise ValueError("Сумма должна быть положительным числом")
        ...

    def salary_decrease(self, name, decrease: float) -> None:
        """
                Уменьшение зарплаты
                :param decrease: на сколько уменьшаем зарпату
                :raise ValueError: Если сумма, на которую уменьшаем з/п, больше з/п, то вызываем ошибку
                Примеры:
                >>> employee1 = Employee('Иван Иванов', 'salesman', 45000)
                >>> employee1.salary_decrease('Иван Иванов', 1000)
                """
        if not isinstance(decrease, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if decrease < 0:
            raise ValueError("Сумма должна положительным числом")
        ...

    def change_position(self, name, new_position) -> None:
        """
                Меняем должность сотрудника
                :param new_position: новая должность
                >>> employee1 = Employee('Иван Иванов', 'salesman', 45000)
                >>> employee1.change_position('Иван Иванов', 'manager')
                """

class Worker(Employee):
    def __init__(self, name: str, position: str, salary: float, hours: int):
        """
                Создание и подготовка к работе объекта "Рабочий"
                :param name: имя рабочего
                :param position: специальность рабочего
                :param salary: оплата в час
                :param hours: количество проработанных часов
                Примеры:
                >>> worker1 = Worker('Владимир','сантехник', 500, 20)  # инициализация экземпляра класса
                """
        super().__init__(name, position, salary)
        if not isinstance(hours, int):
            raise TypeError("Количество проработанных часов должно быть целым числом")
        if hours <= 0:
            raise ValueError("Количество проработанных часов должно быть положительным числом")
        self.hours = hours

    def __str__(self):
        return f"Рабочий {self.name}, {self.position} с почасовой оплатой {self.salary} проработал {self.hours}"

    def __repr__(self):
        return super().__repr__(self)

    def payment(self):
        """
                Оплата труда
                Примеры:
                >>> employee1 = Worker('Владимир','сантехник', 500, 20)
                >>> employee1.payment()
                'Выплатить рабочему Владимир 10000 рублей'
                """
        paym = self.salary * self.hours
        return f'Выплатить рабочему {self.name} {paym} рублей'


if __name__ == "__main__":
    doctest.testmod()
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super.__init__(name, author)
        if pages is not int:
            raise TypeError("Количество страниц должно быть целым числом")
        elif pages <=0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self.pages = pages

    def __str__(self):
        sstr = super().__str__()
        return f"{sstr}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super.__init__(name, author)
        if duration is not float:
            raise TypeError("Продолжительность должна быть типа float")
        elif duration <=0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self.duration = duration

    def __str__(self):
        sstr = super().__str__()
        return f"{sstr}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
class ExceptionManual(Exception):
    """ Общий класс пользовательских исключений """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная ошибка"


class ExceptionZeroQuantity(ExceptionManual):
    """ Класс исключений для добавления товара с нулевым количеством """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Нельзя добавить товар с нулевым количеством"

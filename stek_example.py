# stack_example.py

class Stack:
    """
    Класс Stack реализует структуру данных "стек" с методами push, pop, peek, is_empty и size.
    Стек работает по принципу LIFO (последний вошел — первый вышел).
    """

    def __init__(self):
        # Инициализируем пустой список для хранения элементов стека
        self.items = []

    def push(self, item):
        """
        Добавляет элемент item на вершину стека.
        :param item: добавляемый элемент.
        """
        self.items.append(item)

    def pop(self):
        """
        Удаляет и возвращает элемент с вершины стека.
        :return: элемент с вершины стека или None, если стек пуст.
        """
        if not self.is_empty():
            return self.items.pop()
        return None  # Возвращаем None, если стек пуст

    def peek(self):
        """
        Возвращает элемент на вершине стека без удаления.
        :return: элемент на вершине стека или None, если стек пуст.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """
        Проверяет, пуст ли стек.
        :return: True, если стек пуст, иначе False.
        """
        return len(self.items) == 0

    def size(self):
        """
        Возвращает количество элементов в стеке.
        :return: количество элементов в стеке.
        """
        return len(self.items)


# Пример использования стека
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(35)
    print("Верхний элемент стека:", stack.peek())  # Ожидается 30
    print("Размер стека:", stack.size())  # Ожидается 3
    print("Удаление элемента:", stack.pop())  # Удаляем 30
    print("Новый верхний элемент стека:", stack.peek())  # Ожидается 20
    print("Стек пуст?", stack.is_empty())  # Ожидается False

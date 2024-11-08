# queue_example.py

class Queue:
    """
    Класс Queue реализует структуру данных "очередь" с методами enqueue, dequeue, is_empty и size.
    Очередь работает по принципу FIFO (первый вошел — первый вышел).
    """

    def __init__(self):
        # Инициализируем пустой список для хранения элементов очереди
        self.items = []

    def enqueue(self, item):
        """
        Добавляет элемент item в конец очереди.
        :param item: добавляемый элемент.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Удаляет и возвращает элемент из начала очереди.
        :return: элемент из начала очереди или None, если очередь пуста.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None  # Возвращаем None, если очередь пуста

    def is_empty(self):
        """
        Проверяет, пуста ли очередь.
        :return: True, если очередь пуста, иначе False.
        """
        return len(self.items) == 0

    def size(self):
        """
        Возвращает количество элементов в очереди.
        :return: количество элементов в очереди.
        """
        return len(self.items)


# Пример использования очереди
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Первый")
    queue.enqueue("Второй")
    queue.enqueue("Третий")
    print("Первый элемент в очереди:", queue.items[0])  # Ожидается "Первый"
    print("Размер очереди:", queue.size())  # Ожидается 3
    print("Удаление из очереди:", queue.dequeue())  # Удаляем "Первый"
    print("Новый первый элемент в очереди:", queue.items[0])  # Ожидается "Второй"
    print("Очередь пуста?", queue.is_empty())  # Ожидается False

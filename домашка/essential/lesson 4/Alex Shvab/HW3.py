"""
Пример реализации списка с итератором
"""


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def clear(self):
        """Очистка списка"""
        node = self._head
        while node is not None:
            node_next = node.next
            del node
            node = node_next

        self._head = None
        self._tail = None
        self._length = 0

    def add_index(self, index, value):
        if 0 > index > len(self):
            raise IndexError("Index out of range")
        if index == len(self):
            self.append(value)
        else:
            res = []
            for i in range(len(self)):
                if i == index:
                    res.append(value)
                res.append(self[i])

            self.clear()
            for i in range(len(res)):
                self.append(res[i])

    def del_index(self, index):
        index -= 1
        if 0 > index > len(self):
            raise IndexError("Index out of range")
        else:
            res = []
            for i in range(len(self)):
                if i == index:
                    continue
                res.append(self[i])

            self.clear()
            for i in range(len(res)):
                self.append(res[i])

    def del_last(self):
            res = []
            for i in range(len(self)):
                if i == len(self) - 1:
                    break
                res.append(self[i])

            self.clear()
            for i in range(len(res)):
                self.append(res[i])

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам
        # последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)
    print()

    my_list.add_index(2, 10)
    print(my_list)
    print()

    my_list.del_index(1)
    print(my_list)
    print()

    my_list.del_last()
    print(my_list)
    print()

    my_list.clear()
    print(my_list)
    print()

    # Обход списка
    for element in my_list:
        print(element)

    print()

    # Повторный обход списка
    for element in my_list:
        print(element)


if __name__ == '__main__':
    main()
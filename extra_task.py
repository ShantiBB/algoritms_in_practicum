"""При планировании межпланетной миссии в марсоход «зашили» ежедневные планы 
работ — списки задач на каждый день. Но в реальности оказалось, что планы 
слишком объёмны: марсоход не успевает выполнить за день все запланированные 
задачи.

В Центре управления марсоходами решили сократить ежедневный объём работ. Для 
этого марсоход ежедневно должен удалять из своего дневного расписания одну 
задачу. Какую именно задачу удалить — определяют в ЦУМе. Договориться толком
руководители Центра не смогли и каждый день бросают жребий, случайным образом 
выбирая задачу для удаления. Индекс удаляемого задания передаётся марсоходу.

Технические условия задания
Перечень заданий хранится в связном списке.

Для выполнения задания используйте прекод.

Напишите функцию solution(), которая принимает на вход голову связного списка 
и индекс элемента. Функция должна удалить из списка элемент с указанным 
индексом и вернуть голову обновлённого списка.

В этой задаче не нужно считывать входные данные.

Отправка на проверку
При отправке решения на проверку должен быть выбран компилятор Make.
Решение нужно отправить в файле (не через форму), это строгое условие.
Файл должен быть с расширением .py и не должен называться solution.py.
При нарушении этих условий даже корректно написанное решение не пройдёт тесты.

Формат ввода Функция принимает голову списка и индекс элемента, который надо 
удалить (нумерация с нуля). Список содержит не более 5000 элементов. Список не 
бывает пустым.

Следуйте следующим правилам при отправке решений:

По умолчанию выбран компилятор Make
Решение нужно отправлять в виде файла с расширением .py
Имя solution.py использовать нельзя, назовите, например, my_solution.py
Формат вывода
Функция должна вернуть голову связного списка, в котором удалён нужный элемент.
"""

# Импорт модуля os из стандартной библиотеки
# для взаимодействия с операционной системой.
import os

# Считывание переменной окружения REMOTE_JUDGE, чтобы определить,
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    count = 0
    head_node = node
    prev_node = node
    if idx == 0:
        return head_node.next_item
    while count < idx:
        prev_node = node
        node = node.next_item
        count += 1
    prev_node.next_item = node.next_item
    return head_node


# Тестирующая функция для проверки решения.
# Не изменяйте её, она не требует вашего внимания.
def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    # Выражение, начинающееся с ключевого слова assert,
    # проверяет, что утверждение в выражении истинно.
    # Если утверждение ложно - в этом месте возникнет ошибка.
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()

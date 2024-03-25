"""
При путешествии по планете марсоход постоянно замеряет высоту рельефа и 
сохраняет результаты замеров в массив.

Одна из задач марсохода — поиск «правильных гор». «Правильной» считается та 
гора, у которой на пути от подножия до вершины высота постоянно растёт, а на 
пути от вершины к подножию — постоянно уменьшается. Если у горы есть несколько
вершин или в каком-то месте встречается горизонтальный участок — это 
«неправильная гора».

Напишите функцию valid_mountain_array, которая будет принимать на вход массив 
с высотами и возвращать True или False в зависимости от того, «правильная» это 
гора или нет.

Если в массиве менее трёх элементов, такой массив не может описывать 
«правильную» гору.

Формат ввода
Массив целых чисел через пробел — отметки о высоте точек рельефа.

Формат вывода
Булево значение: True — если гора «правильная», False — если гора 
«неправильная».
"""


a = input()


def valid_mountain_array(array):
    array = [int(i) for i in array.split()]
    max_value = max(array)
    left_part = array[:array.index(max_value)]
    right_part = array[array.index(max_value):]
    if len(array) < 3 or len(right_part) <= 1 or len(left_part) == 0:
        return False
    if (
            left_part == sorted(left_part)
            and len(left_part) == len(set(left_part))
    ):
        if (
                right_part == sorted(right_part, reverse=True)
                and len(right_part) == len(set(right_part))
        ):
            return True
    return False


print(valid_mountain_array(a))

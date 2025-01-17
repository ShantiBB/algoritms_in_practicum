"""Марсоход должен исследовать странные каменные структуры: на поверхности 
скал обнаружена последовательность символов. Предположительно, эту 
последовательность создали разумные существа. Учёные предполагают, что эта 
последовательность содержит некие коды или тексты.

Для расшифровки необходимо выявить в последовательности самую длинную 
подстроку, состоящую из уникальных символов: наибольший ряд символов, в 
котором каждый символ встречается только один раз. Это поможет найти ключ к 
разгадке послания или просто даст понять, случайны ли эти символы, или в них 
есть порядок.

Напишите программу, которая принимает на вход строку и находит в ней 
наибольшую длину подстроки, в которой нет повторяющихся символов. Программа 
должна вернуть натуральное число — длину этой подстроки.

Используйте метод скользящего окна для решения задачи. Если в строке 
встретится дубликат, запомните длину получившейся подстроки и начинайте 
строить окно заново.

Формат ввода
Одна строка, состоящая из строчных латинских букв. Длина строки не превосходит 
10 000 символов.

Формат вывода
Натуральное число — длина наибольшей подстроки с уникальными символами.
"""


def find_longest_unique_substring(s):
    if not s:
        return 0

    max_length = 0
    start = 0
    seen = {}

    for i, char in enumerate(s):
        if char in seen:
            start = max(start, seen[char] + 1)
        seen[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length


# Пример использования
print(find_longest_unique_substring(input()))

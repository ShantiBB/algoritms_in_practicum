# id посылки 110524447
def encrypted_instructions(instructions: str) -> str:  
    """Функция принимает сокращенный вид инструкций, где каждая инструкция
    имеет набор параметров, если набор повторяется, тогда он записывается в
    квадратных скобках и перед ним ставится множитель повторений. Функция
    возвращает полный набор инструкций.
    """
    result, multiplier, stack = '', '', []
    for char in instructions:
        if char.isdigit():
            multiplier += char
        elif char == '[':
            stack.append((multiplier, result))
            result, multiplier = '', ''
        elif char == ']':
            num, instruction = stack.pop()
            result = instruction + int(num) * result
        else:
            result += char
    return result


if __name__ == '__main__':
    print(encrypted_instructions(input()))

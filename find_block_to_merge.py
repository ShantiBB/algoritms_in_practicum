def find_block_to_merge(n_arr, arr):
    """Массив разделяется на блоки так, чтобы каждый блок можно было 
    отсортировать.
    Первый блок обязательно должен содержать 0. Если длина первого блока — r 
    элементов,
    то максимальным значением в первом блоке должно быть число r - 1. А 
    следующий блок (если он вообще будет) должен содержать число r.
    """
    array_list = list(map(int, arr.split()))
    result_block = {}
    count_block = 0
    left = 0
    right = 1
    while right <= n_arr:
        # Проверка условий для первого блока
        result = array_list[left: right]
        if (
                0 in result
                and max(result) == len(result) - 1
                and sum(result) == sum(range(max(result) + 1))
        ):
            result_block[count_block] = result
            count_block += 1
            left = right
        # Проверка условий для остальных блоков
        elif (
                array_list[right - 1] in array_list[:right]
                and sum(array_list[left:right]) 
                == sum(range(right)) - sum(range(left))
        ):
            result_block[count_block] = result
            count_block += 1
            left = right
        right += 1
    print(count_block)
    return result_block


print(find_block_to_merge(4, '0 1 3 2'))
print(find_block_to_merge(8, '3 6 7 4 1 5 0 2'))
print(find_block_to_merge(5, '1 0 2 3 4'))

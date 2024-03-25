def count_limit_weight(weights: str, limit: int):
    weights = sorted([int(weight) for weight in weights.split()])

    if any(weight > limit for weight in weights):
        return 'Вес одного из роботов превышает лимит.'

    count_platforms, left, right = 0, 0, len(weights)

    while left < right:

        count_platforms += 1

        right -= 1

        if weights[left] + weights[right] <= limit:
            left += 1

    return count_platforms


if __name__ == '__main__':
    mass, lim = input(), int(input())

    print(count_limit_weight(mass, lim))
    # ID посылки - 109722827

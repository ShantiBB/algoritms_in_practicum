# def min_stone_weight(n_users, users_weight, n_weight, weight):
#     users_weight.sort()
#     weight.sort()
#     left = 0
#     right = 0
#     count = 0
#     while left < n_users and right < n_weight:
#         if users_weight[left] <= weight[right]:
#             left += 1
#             count += 1
#         right += 1
#     return count
#
#
# print(min_stone_weight(
#     int(input()),
#     list(map(int, input().split())),
#     int(input()),
#     list(map(int, input().split()))
# ))


def min_stone_weight(
        n_users,
        users_weight,
        n_weight,
        weight,
        left=0,
        right=0,
        count=0
):

    if left >= n_users or right >= n_weight:
        return count

    if users_weight[left] <= weight[right]:
        return min_stone_weight(
            n_users,
            users_weight,
            n_weight,
            weight,
            left + 1,
            right + 1,
            count + 1
        )
    else:
        return min_stone_weight(
            n_users,
            users_weight,
            n_weight,
            weight,
            left,
            right + 1,
            count
        )


print(min_stone_weight(
    int(input()),
    sorted(list(map(int, input().split()))),
    int(input()),
    sorted(list(map(int, input().split())))
))

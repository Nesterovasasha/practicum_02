def share_sweets(N, M):
    sweets_per_friend = M // (N + 1)
    remaining_sweets = M % (N + 1)

    return sweets_per_friend

friends_and_sweets = (input("Введите количество друзей и конфет через пробел: "))
N, M = map(int, friends_and_sweets.split())

result = share_sweets(N, M)
print(result)
# freq_map: dict[tuple[int, int], int] = {}


# intervals = [(3, 5), (4, 9), (5, 8)]
# intervals2 = [
#     (1, 9),
#     (3, 7),
#     (3, 12),
#     (4, 19),
#     (4, 5),
#     (6, 13),
#     (14, 19),
#     (1, 2),
#     (3, 9),
# ]
# # intervals3 = [(1, 8), (7, 9), (2, 4)]

intervals = []
n: int = int(input())
for i in range(n):
    user_input = input()
    start = []
    for idx, char in enumerate(user_input):
        if char == " ":
            break
        start.append(char)
    start = int("".join(start))
    end = user_input[idx + 1 :]
    end = int(end)
    intervals.append((start, end))


def movie_fest(intervals: list) -> int:
    intervals.sort(key=lambda x: x[1])
    result = []
    for k in intervals:
        flag = True
        for key in result:
            if k[1] > key[0] and k[0] < key[1]:
                flag = False
                break
        if flag:
            result.append(k)
    return len(result)


print(movie_fest(intervals))

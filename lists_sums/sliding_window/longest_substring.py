# requirements:
# 1. no repeating characters

# approach 1
# brute force
# current index se forward jana hai
# condition: until already character mila
# har ek index keliye ek substring
# compare them to get the best
# time complexity- o(n*n)


def longest_substring_brute_force(target: str):
    start = 0
    end = 0
    for idx in range(len(target)):
        seen = {}
        seen[target[idx]] = True

        for inner_idx in range(idx + 1, len(target)):
            if target[inner_idx] in seen:
                if end - start < inner_idx - 1 - idx:
                    start = idx
                    end = inner_idx - 1
                break
            print(f"{target[inner_idx]} is not seen")
            seen[target[inner_idx]] = True
        print(f"end={end}, start={start}")
        print(f"longest substring for {target[idx]}: {target[idx:end+1]}")
    print(f"the longest substring is {target[start:end+1]}")


# longest_substring_brute_force("hiiyi")


def longest_substring_sliding_window(target: str):
    left = 0
    right = 1
    max_left = 0
    max_right = 0
    seen = {}
    seen[target[left]] = 0

    while right < len(target):
        char = target[right]

        if char in seen and seen[char] >= left:
            print(f"longest substring for {target[left]}: {target[left:right]}")
            left = seen[char] + 1

        if right - left > max_right - max_left:
            max_right = right
            max_left = left
        seen[char] = right
        right += 1
    print(f"the longest substring is {target[max_left : max_right + 1]}")


# longest_substring_sliding_window("hiiyawelii")


arr = [1, 6, 2, 4, 8, 3]


# bruteforce
def prev_smaller_element(arr: list) -> list:
    result = [-1] * len(arr)
    for curr_idx in range(len(arr) - 1, -1, -1):
        for inner_idx in range(curr_idx - 1, -1, -1):
            if arr[curr_idx] > arr[inner_idx]:
                result[curr_idx] = arr[inner_idx]
                break
    return result


# optimal-stack
def prev_smaller_element(arr: list) -> list:
    result = []
    stack = []
    for idx in range(len(arr)):
        while stack and stack[-1] > arr[idx]:
            stack.pop()
        prev_min = stack[-1] if stack else -1
        result.append(prev_min)
        stack.append(arr[idx])
    return result


print(prev_smaller_element(arr))

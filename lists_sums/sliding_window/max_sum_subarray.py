# requirements
# given k and an array
# return subaary of size k whose sum is max

# approach
# get initial sum of k elements
# put left at 0 and right at k-1
# add right element, subtract left element
# if new sum greater than prev sum update flags


def max_sum_subarray(arr: list, k: int):
    left = 0
    max_left = 0
    max_right = k - 1
    prev_sum = 0
    for idx in range(k):
        prev_sum += arr[idx]
    max_sum = prev_sum
    for right in range(k, len(arr)):
        window_sum = prev_sum + arr[right] - arr[left]
        left += 1
        if window_sum > max_sum:
            max_sum = window_sum
            max_left = left
            max_right = right
        prev_sum = window_sum
    print(f"the subarrray is from {max_left} to {max_right} with sum {max_sum}")

max_sum_subarray([1, 6, 2, 7, 9, -1], 3)

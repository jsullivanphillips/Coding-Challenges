# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10],
# return 4 and 8. The order does not matter.

# Use set difference two find the answer in one pass
def find_non_repeating(arr):
    existing_chars = []
    not_answer_arr = []
    for char in arr:
        if char not in existing_chars :
            existing_chars.append(char)
        else:
            not_answer_arr.append(char)
    print(list(set(existing_chars) - set(not_answer_arr)))

arr = [2, 4, 6, 8, 10, 2, 6, 10]
find_non_repeating(arr)

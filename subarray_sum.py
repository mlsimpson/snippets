def find_subarray(arr, target_sum):

    # create an empty map
    prefix_map = {}

    # create empty subarray to return
    sub_arr = []

    # Maintains sum of elements so far
    curr_sum = 0

    for i in range(0, len(arr) - 1):
        # add current element to curr_sum
        curr_sum = curr_sum + arr[i]

        # if curr_sum is equal to target sum
        # we found a subarray starting from index 0
        # and ending at index i
        if curr_sum == target_sum:
            sub_arr = arr[0:(i + 1)]
            print("about to return: curr_sum =", curr_sum, \
                    "(curr_sum - target_sum) =", curr_sum - target_sum, ":: prefix_map", prefix_map)
            return sub_arr


        # If curr_sum - sum already exists in map
        # we have found a subarray with target sum
        if (curr_sum - target_sum) in prefix_map:
            start  = prefix_map[curr_sum - target_sum] + 1
            sub_arr = arr[start:(i + 1)]
            print("about to return: curr_sum =", curr_sum, \
                    "(curr_sum - target_sum) =", curr_sum - target_sum, ":: prefix_map", prefix_map)
            return sub_arr

        prefix_map[curr_sum] = i

        print("curr_sum =", curr_sum, "(curr_sum - target_sum) =", \
                curr_sum - target_sum, ":: prefix_map", prefix_map)

    # If we reach here, then no subarray exists
    print("No subarray with given sum exists")


if __name__ == "__main__":

    arr = [2, 1, 10, 2, -2, -20, 10]
    target_sum = -10

    print(find_subarray(arr, target_sum))


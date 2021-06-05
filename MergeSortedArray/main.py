class MergeSortedArray:
    def test_merge_arrays(self, function):
        list_of_nums = [[[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3], [[1], 1, [], 0], [[0], 0, [1], 1], ]
        ground_truth_list = [[1, 2, 2, 3, 5, 6], [1], [1], ]
        for i, arg in enumerate(list_of_nums):
            function(*arg)
            if arg[0] == ground_truth_list[i]:
                print('Test{0} ---- Passed'.format(i))
            else:
                print('Test{0} ---- Failed'.format(i))

    def merge_arrays(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        Do not return anything, modify nums1 in-place instead.
        nums1.length == m + n
        nums2.length == n
        0 <= m, n <= 200
        1 <= m + n <= 200
        -109 <= nums1[i], nums2[j] <= 109
        """
        total_length = m + n
        total_nums = []
        nums1_counter = 0
        nums2_counter = 0
        for i in range(total_length):
            if nums1_counter == m or nums2_counter == n:
                break
            else:
                if nums1[nums1_counter] < nums2[nums2_counter]:
                    total_nums.append(nums1[nums1_counter])
                    nums1_counter += 1
                else:
                    total_nums.append(nums2[nums2_counter])
                    nums2_counter += 1
        if nums1_counter != m and nums2_counter == n:
            total_nums.extend(nums1[nums1_counter:m])
        elif nums1_counter == m and nums2_counter != n:
            total_nums.extend(nums2[nums2_counter:n])
        for i in range(total_length):
            nums1[i] = total_nums[i]

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


test = MergeSortedArray()
test.test_merge_arrays(test.merge)
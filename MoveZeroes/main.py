class MoveZeroes:
    def test_move_zeroes(self, function):
        test_cases = [[0, 1, 0, 3, 12], [0], [], [0, 0, 1], ]
        right_results = [[1, 3, 12, 0, 0], [0], [], [1, 0, 0], ]
        for i, case in enumerate(test_cases):
            function(case)
            if case == right_results[i]:
                print('Test{0} --- Passed'.format(i))
            else:
                print("Test{0} --- Failed".format(i))

    def movezeroes(self, nums: list[int]) -> None:
        """Inplace changes array of
        integer numbers
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)


test = MoveZeroes()
test.test_move_zeroes(test.movezeroes)
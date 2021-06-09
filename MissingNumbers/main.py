class MissingNumbers:
    def test_missingnumber(self, function):
        test_cases = [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1], [0], ]
        right_answers = [2, 2, 8, 1, ]
        for i, case in enumerate(test_cases):
            if function(case) == right_answers[i]:
                print("Test{0} --- Passed".format(i))
            else:
                print("Test{0} --- Failed".format(i))

    def missingnumber(self, nums: list[int]) -> int:
        """Returns missing value of array [0,n].
        Formula for sum of arithmetic progression Sn  =(a1 + an)/2 * n
        """
        sum_progression = int((len(nums) * (len(nums) + 1)) / 2)
        return sum_progression - sum(nums)


test = MissingNumbers()
test.test_missingnumber(test.missingnumber)
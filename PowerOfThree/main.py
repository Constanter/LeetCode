class PowersOfThree:
    def isPowerOfThree(self, n: int) -> bool:
        counter = 1
        while True:
            if counter > n:
                return False
            elif counter == n:
                return True
            else:
                counter *= 3

    def test_power_of_three(self, function):
        test_cases = [9, 0, 45, 1, 77, 81, ]
        right_aswers = [True, False, False, True, False, True, ]
        for i, case in enumerate(test_cases):
            if function(case) == right_aswers[i]:
                print("Test{0} --- Passed")
            else:
                print("Test{0} --- Failed")

test = PowersOfThree()
test.test_power_of_three(test.isPowerOfThree)
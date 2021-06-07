import re


class ValidPalindrome:
    def test_valid_palindrome(self, function):
        test_cases = ["A man, a plan, a canal: Panama", "race a car", '', ]
        right_answers = [True, False, True, ]
        for i, answer in enumerate(test_cases):
            if function(answer) == right_answers[i]:
                print("Test{0} --- Passed".format(i))
            else:
                print("Test{0} --- Failed".format(i))

    def valid_palindrom(self, s: str) -> bool:
        """Get a string, and return True if string is palindrome,
        or return False if is not.We are ignoring cases, and non alphanumeric symbols
        """
        result_string = "".join([x for x in s if x.isalnum()]).lower()
        return result_string == result_string[::-1]

    def optimal_valid_palindrom(self, s: str) -> bool:
        s1 = re.sub("[^0-9a-zA-Z]+", "", s).lower()

        start, end = 0, len(s1) - 1

        while start < end:
            if s1[start] != s1[end]:
                return False
            start += 1
            end -= 1

        return True


test = ValidPalindrome()
test.test_valid_palindrome(test.valid_palindrom)
test.test_valid_palindrome(test.optimal_valid_palindrom)
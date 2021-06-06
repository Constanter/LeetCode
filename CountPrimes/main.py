class CountPrimes:
    def test_count_primes(self, function):
        list_of_numbers = [0, 1, 2, 5, 10, -1, ]
        number_of_correct_numbers = [0, 0, 1, 3, 4, 'Assert_Error', ]
        for i, number in enumerate(list_of_numbers):
            if function(number) == number_of_correct_numbers[i]:
                print('Test{0} ---- Passed'.format(i))
            else:
                print('Test{0} ---- Failed'.format(i))

    def countprimes(self, n: int) -> int:
        """Program have to return quantity of prime numbers,
        less than n.
        0 <= n <= 5 * 10^6.
        """
        assert n >= 0, 'n must be greater than 0'
        counter = 0
        if n < 2:
            return 0
        elif n == 2:
            return 1
        else:
            for i in range(3, n+1, 2):
                pass


test = CountPrimes()
test.test_count_primes(test.countprimes)
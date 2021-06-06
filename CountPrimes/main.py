class CountPrimes:
    def test_count_primes(self, function):
        list_of_numbers = [0, 1, 2, 3, 5, 10, -1, ]
        number_of_correct_numbers = [0, 0, 0, 1, 2, 4, 'Assert_Error', ]
        for i, number in enumerate(list_of_numbers):
            if function(number) == number_of_correct_numbers[i]:
                print('Test{0} ---- Passed'.format(i))
            else:
                print('Test{0} ---- Failed'.format(i))
                print(function(number))

    def countprimes(self, n: int) -> int:
        """Program have to return quantity of prime numbers,
        less than n.
        0 <= n <= 5 * 10^6.
        """
        assert n >= 0, 'n must be greater than 0'
        counter = [2, ]
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        else:
            for number in range(3, n, 2):
                flag = True
                for primes in counter:
                    if primes > int(number**0.5) + 1:
                        break
                    elif number % primes == 0:
                        flag = False
                        break
                if flag:
                    counter.append(number)
            return len(counter)


test = CountPrimes()
test.test_count_primes(test.countprimes)
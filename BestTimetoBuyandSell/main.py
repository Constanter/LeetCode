class BestBuyAndSell:
    def test_max_profit(self, function):
        test_cases = [[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1], ]
        correct_answers = [7, 4, 0]
        for i, case in enumerate(test_cases):
            if function(case) == correct_answers[i]:
                print("Test{0} --- Passed".format(i))
            else:
                print("Test{0} --- Failed".format(i))

    def maxProfit(self, prices: list[int]) -> int:
        """"Finds maximum profit you can achieve,as difference between
        [i + 1] and [i] elements.
        """
        counter = 0
        for i in range(len(prices) - 1):
            counter += max(0, prices[i+1] - prices[i])
        return counter

test = BestBuyAndSell()
test.test_max_profit(test.maxProfit)
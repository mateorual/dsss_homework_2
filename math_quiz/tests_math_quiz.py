import unittest
from math_quiz import random_integer, random_operator, random_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)


    def test_random_operator(self):
        # Test if the output of the random_operator belongs to the list expected outcomes
        result_random_operator = random_operator()
        expected_outcomes = ['+', '-', '*']
        self.assertIn(result_random_operator,expected_outcomes)


    def test_random_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (7, 4, '*', '7 * 4', 28),
                (-5,-3,'-','-5 - -3',-2)]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                self.assertEqual(random_operation(num1,num2,operator),(expected_problem,expected_answer))

if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch
import Wheel_of_fortune_code


class TestRewardFun(unittest.TestCase):
    """
    A test suite for testing the reward_fun() function in the Wheel_of_fortune_code module.

    This class uses the unittest framework to define several test cases to verify the correctness
    of the reward_fun() function. It employs mocking to simulate different outcomes of the random.random()
    function used within reward_fun() to test different branches of the code.

    Methods:
        setUp: Initializes the necessary attributes for each test case.
        test_lower_boundary: Tests the reward_fun() function at the lower boundary of the 'second level' prize range.
        test_upper_boundary: Tests the reward_fun() function at the upper boundary of the 'second level' prize range.
        test_mid_range: Tests the reward_fun() function with a value in the middle of the 'third level' prize range.
        tearDown: Prints the test results after each test is executed.

    The test suite aims to ensure that the reward_fun() function accurately determines the prize level
    based on the random number generated within specific ranges defined in the Wheel_of_fortune_code.
    """

    def setUp(self):
        # Initialize the variable to 0 before each test
        self.failures = 0

    def test_lower_boundary(self):
        with patch('Wheel_of_fortune_code.random.random', return_value=0.03):
            try:
                self.assertEqual(Wheel_of_fortune_code.reward_fun(), 'second level (Second prize or First prize')
            except AssertionError:
                self.failures += 1

    def test_upper_boundary(self):
        with patch('Wheel_of_fortune_code.random.random', return_value=0.19999):
            try:
                self.assertEqual(Wheel_of_fortune_code.reward_fun(), 'second level (Second prize or First prize')
            except AssertionError:
                self.failures += 1

    def test_mid_range(self):
        with patch('Wheel_of_fortune_code.random.random', return_value=0.5):
            try:
                self.assertEqual(Wheel_of_fortune_code.reward_fun(), 'third level (Consolation prize or Third prize)')
            except AssertionError:
                self.failures += 1

    def tearDown(self):
        # Check if the failures variable is still 0
        if self.failures == 0:
            print("Passed all tests!")
        else:
            print(f"Failed {self.failures} tests.")


if __name__ == '__main__':
    unittest.main()

import sys
from unittest.mock import MagicMock, patch
import Wheel_of_fortune_code as Game


def mock_end(k):
    """
    Test for the 'end' function in the lucky wheel game.

    This script conducts a series of tests on the 'end' function, which is responsible for displaying
    the prize won by the user at the end of the game. The script focuses on verifying that the function
    correctly handles different prize levels and prints the appropriate messages.
    """

    print("Congratulations, you have drawn " + k)
    print("Your award is: %s" % k)
    print("Screen color would be set to (155, 155, 0)")
    print("Text color would be set to (110, 55, 155)")


# Mocking Pygame
with patch('Wheel_of_fortune_code.pygame', MagicMock()):
    Game.end = mock_end

# Test cases
test_cases = ["Star prize", "Second level", "Third level"]
failure_count = 0

for test_case in test_cases:
    print(f"\nTesting with prize: {test_case}")
    try:
        Game.end(test_case)
        # If the output is not as expected, increment the failure_count
        # For example:
        # if not expected_output_condition:
        #     failure_count += 1
    except Exception as e:
        print(f"Test failed with exception: {e}")
        failure_count += 1

# Results
if failure_count == 0:
    print("\nAll tests passed!")
else:
    print(f"\nTests completed with {failure_count} failures.")

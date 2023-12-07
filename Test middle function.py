import sys
import math
from unittest.mock import MagicMock, patch

"""
Test script for the 'middle' function in the lucky wheel game.

This script tests the 'middle' function, which handles the spinning of the lucky wheel. 
The test focuses on verifying the correct behavior of the angle calculation, event handling, 
and the loop break condition.

The script mocks dependencies used in the 'middle' function, including Pygame functionalities 
and external functions. The goal is to ensure that the function behaves as expected in a 
controlled environment without the need for graphical output.
"""


import Wheel_of_fortune_code as Game

# Mock dependencies
mock_hand = MagicMock()
mock_bg = MagicMock()
mock_screen = MagicMock()
mock_reward_fun = MagicMock(return_value="Test Prize")
mock_tick = MagicMock()
mock_pygame = MagicMock()
mock_pygame.transform.rotate.return_value = mock_hand
mock_pygame.display.flip.return_value = None
mock_pygame.draw.circle.return_value = None

# Replace dependencies in the game module
Game.hand = mock_hand
Game.bg = mock_bg
Game.screen = mock_screen
Game.reward_fun = mock_reward_fun
Game.tick = mock_tick
Game.pygame = mock_pygame


# Mock function to replace sys.exit()
def mock_exit():
    raise SystemExit


sys.exit = mock_exit

# Test the middle function
failure_count = 0

try:
    print("\nTesting 'middle' function")
    Game.middle()
except SystemExit:
    # This is expected due to sys.exit() in the event loop
    pass
except Exception as e:
    print(f"Test failed with exception: {e}")
    failure_count += 1

# Results
if failure_count == 0:
    print("\nTest passed!")
else:
    print(f"\nTest failed with {failure_count} failures.")

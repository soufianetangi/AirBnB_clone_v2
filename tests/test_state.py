# /AirBnB_clone_v2/tests/test_state.py
import unittest
from models.state import State

class TestState(unittest.TestCase):
    
    def test_state_creation(self):
        state = State("California", "CA")
        self.assertEqual(state.name, "California")
        self.assertEqual(state.state_code, "CA")

if __name__ == '__main__':
    unittest.main()

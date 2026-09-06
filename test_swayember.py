# test_swayember.py
"""
Tests for SwayEmber module.
"""

import unittest
from swayember import SwayEmber

class TestSwayEmber(unittest.TestCase):
    """Test cases for SwayEmber class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SwayEmber()
        self.assertIsInstance(instance, SwayEmber)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SwayEmber()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

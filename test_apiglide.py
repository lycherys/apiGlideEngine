# test_apiglide.py
"""
Tests for apiGlide module.
"""

import unittest
from apiglide import apiGlide

class TestapiGlide(unittest.TestCase):
    """Test cases for apiGlide class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = apiGlide()
        self.assertIsInstance(instance, apiGlide)
        
    def test_run_method(self):
        """Test the run method."""
        instance = apiGlide()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_chainworld.py
"""
Tests for ChainWorld module.
"""

import unittest
from chainworld import ChainWorld

class TestChainWorld(unittest.TestCase):
    """Test cases for ChainWorld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainWorld()
        self.assertIsInstance(instance, ChainWorld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainWorld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

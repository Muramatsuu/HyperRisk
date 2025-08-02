# test_hyperrisk.py
"""
Tests for HyperRisk module.
"""

import unittest
from hyperrisk import HyperRisk

class TestHyperRisk(unittest.TestCase):
    """Test cases for HyperRisk class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HyperRisk()
        self.assertIsInstance(instance, HyperRisk)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HyperRisk()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

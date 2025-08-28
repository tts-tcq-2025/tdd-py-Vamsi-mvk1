"""
Test runner for StringCalculator
This file is expected by the GitHub Actions workflow
"""

import unittest
import sys
import os

# Add current directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import all our test modules
from test_string_calculator import TestStringCalculator
from test_edge_cases import TestStringCalculatorEdgeCases


if __name__ == '__main__':
    # Create test loader and suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Collect tests from both classes
    suite.addTests(loader.loadTestsFromTestCase(TestStringCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestStringCalculatorEdgeCases))

    # Run with verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with proper code for CI/CD
    sys.exit(0 if result.wasSuccessful() else 1)

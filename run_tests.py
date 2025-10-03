import unittest
from tests.homework.d_repetition import tests_repetition

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    import sys
    sys.exit(0 if result.wasSuccessful() else 1)

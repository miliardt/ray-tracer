import os
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = os.getcwd()
    suite = loader.discover(start_dir, pattern='*.py')

    runner = unittest.TextTestRunner()
    runner.run(suite)

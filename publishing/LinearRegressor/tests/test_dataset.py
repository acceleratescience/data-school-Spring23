import numpy as np
from typing import Tuple
from sklearn.model_selection import train_test_split
import unittest
import tempfile
import os

from linear_regressor import Dataset

class TestDataset(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset()

    def test_from_csv(self):
    # Create a temporary file with csv data
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as f:
            f.write("1,2,3\n4,5,6\n")
            f.flush()

            self.dataset.from_csv(f.name)

        # Remove the temporary file
        os.unlink(f.name)

        # Check if the data is loaded correctly
        np.testing.assert_array_equal(self.dataset.X, np.array([1, 2, 3]))
        np.testing.assert_array_equal(self.dataset.y, np.array([4, 5, 6]))


    def test_from_numpy(self):
        array = np.array([[1, 4], [2, 5], [3, 6]])
        self.dataset.from_numpy(array)

        # Check if the data is loaded correctly
        np.testing.assert_array_equal(self.dataset.X, np.array([1, 2, 3]))
        np.testing.assert_array_equal(self.dataset.y, np.array([4, 5, 6]))

    def test_test_train_split(self):
        array = np.array([[1, 4], [2, 5], [3, 6]])
        self.dataset.from_numpy(array)

        self.dataset.test_train_split(pct_test=0.5)

        # Check if the data is split correctly using the instance variables
        np.testing.assert_array_equal(self.dataset.X_train, np.array([1]))
        np.testing.assert_array_equal(self.dataset.X_test, np.array([2, 3]))
        np.testing.assert_array_equal(self.dataset.y_train, np.array([4]))
        np.testing.assert_array_equal(self.dataset.y_test, np.array([5, 6]))



if __name__ == '__main__':
    unittest.main()

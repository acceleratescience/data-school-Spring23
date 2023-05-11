import numpy as np
from linear_regressor import Dataset
from linear_regressor import LinearRegressor
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score
import unittest
import tempfile
import os

class TestLinearRegressor(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        X = np.linspace(0, 10, 100)
        y = 3 * X + 5 + np.random.normal(0, 1, 100)
        self.array = np.column_stack((X, y))
        self.dataset = Dataset()
        self.dataset.from_numpy(self.array)
        self.dataset.test_train_split(pct_test=0.5)
        self.regressor = LinearRegressor(self.dataset)


    def test_train(self):
        self.regressor.train()
        self.assertIsNotNone(self.regressor.thetas)

    def test_predict(self):
        self.regressor.train()
        y_pred_test = self.regressor.predict(test=True)
        y_pred_train = self.regressor.predict(test=False)

        self.assertIsNotNone(y_pred_test)
        self.assertIsNotNone(y_pred_train)

    def test_score(self):
        train_score = self.regressor.score(test=False)
        train_pred = self.regressor.predict(test=False)
        expected_train_score = r2_score(self.regressor.dataset.y_train, train_pred)
        self.assertAlmostEqual(train_score, expected_train_score)

        test_score = self.regressor.score(test=True)
        test_pred = self.regressor.predict(test=True)
        expected_test_score = r2_score(self.regressor.dataset.y_test, test_pred)
        self.assertAlmostEqual(test_score, expected_test_score)

    def test_save_coeffs(self):
        self.regressor.train()
        with tempfile.NamedTemporaryFile(suffix=".npy", delete=False) as f:
            temp_path = f.name

        self.regressor.save_coeffs(temp_path[:-4])

        loaded_thetas = np.load(temp_path)
        os.remove(temp_path)

        self.assertTrue(np.allclose(self.regressor.thetas, loaded_thetas, atol=1e-6))


if __name__ == '__main__':
    unittest.main()

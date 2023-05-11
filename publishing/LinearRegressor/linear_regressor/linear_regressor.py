import numpy as np
from typing import Tuple
from sklearn.model_selection import train_test_split


class Dataset():
    def __init__(self) -> None:
        """Dataset initializer.
        """
        self.data = None
        self.X = None
        self.y = None


    def from_csv(self, csv_file : str) -> None:
        """Load a csv file into the dataset.

        Args:
            csv_file (str): Path to the csv file.
        """
        self.data = np.loadtxt(csv_file, delimiter=',').T
        self.X = self.data[:, 0]
        self.y = self.data[:, 1]


    def from_numpy(self, array : np.ndarray) -> None:
        """Load a numpy array into the dataset.

        Args:
            array (np.ndarray): Numpy array where the first column is the X values and the second column is the y values.
        """
        self.data = array
        self.X = self.data[:, 0]
        self.y = self.data[:, 1]


    def test_train_split(self, pct_test : float = 0.2) -> Tuple:
        """Perform a test train split on the dataset.

        Args:
            pct_test (float, optional): Amount of data used in testing. Defaults to 0.2.

        Returns:
            Tuple: Tuple of X_train, X_test, y_train, y_test.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=pct_test, shuffle=False)


class LinearRegressor():
    def __init__(self, dataset : Dataset) -> None:
        self.dataset = dataset
        self.thetas = None


    def train(self) -> None:
        """Train the regression model.
        """
        xs = self.dataset.X_train.reshape(-1, 1)
        ys = self.dataset.y_train.reshape(-1, 1)

        ones = np.ones((xs.shape[0], 1))
        xs = np.concatenate( (ones, xs), axis=1)
        xTx = np.matrix(xs.T @ xs)
        xTxInv = np.array(xTx.I)
        self.thetas = (xTxInv @ xs.T) @ ys
        

    def predict(self, test : bool = True) -> np.ndarray:
        """Predict on the test or train data.

        Args:
            test (bool, optional): If False performs inference on training data
            else performs inference on testing data. Defaults to True.

        Returns:
            np.ndarray: Predicted y values.
        """
        if test:
            X = self.dataset.X_test.reshape(-1, 1)
            X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        else:
            X = self.dataset.X_train.reshape(-1, 1)
            X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)


        return X.dot(self.thetas)


    def score(self, test : bool = True) -> float:
        """Get the score of the model.

        Args:
            test (bool, optional): If False performs scoring on training data
            else performs scoring on testing data. Defaults to True.

        Returns:
            float: R^2 score
        """
        if test:
            corr_matrix = np.corrcoef(self.dataset.X_test, self.dataset.y_test)
        else:
            corr_matrix =  np.corrcoef(self.dataset.X_train, self.dataset.y_train)
        
        corr = corr_matrix[0,1]
        R_sq = corr**2
        
        return R_sq

    def save_coeffs(self, filename : str) -> None:
        """Save the model coefficients to a file.

        Args:
            filename (str): Path to file. Should end in .npy.
        """
        np.save(f'{filename}.npy', self.thetas)
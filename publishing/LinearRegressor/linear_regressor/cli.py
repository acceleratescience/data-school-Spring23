import argparse
import numpy as np
from linear_regressor import Dataset
from linear_regressor import LinearRegressor

def main():
    parser = argparse.ArgumentParser(description="Train a linear regression model and save the coefficients.")
    parser.add_argument("csv_file", type=str, help="Path to the CSV file.")
    parser.add_argument("output_file", type=str, help="Path to the output .npy file for the model coefficients.")
    parser.add_argument("--test_size", type=float, default=0.2, help="Proportion of the dataset to include in the test split (default: 0.2).")
    
    args = parser.parse_args()
    
    # Load data from the CSV file and split into train and test sets
    dataset = Dataset()
    dataset.from_csv(args.csv_file)
    dataset.test_train_split(pct_test=args.test_size)
    
    # Train the linear regressor
    model = LinearRegressor(dataset)
    model.train()
    
    # Save the coefficients
    
    np.save(args.output_file, model.thetas)

if __name__ == "__main__":
    main()

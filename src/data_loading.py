import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path, header=None)
    return data

if __name__ == "__main__":
    data = load_data('../data/your_dataset.csv')
    print(data.head())
# Raw Implementation 

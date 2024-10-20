def preprocess_data(data):
    # Example preprocessing steps
    data.dropna(inplace=True)
    # Additional preprocessing as needed
    return data

if __name__ == "__main__":
    from data_loading import load_data
    data = load_data()
    data = preprocess_data(data)
    print(data.head())

#Also a raw sketch of implementation

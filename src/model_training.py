from data_preprocessing import preprocess_data
from data_loading import load_data
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_model(X_train, y_train):
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    return clf

if __name__ == "__main__":
    data = load_data()
    data = preprocess_data(data)
    
    # Assuming the last column is the label
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Train the model
    clf = train_model(X_train, y_train)
    
    # Evaluate the model
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

#Also a sketch towards implementing the training model

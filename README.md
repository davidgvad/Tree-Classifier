# Tree Classifier Project

![License](https://img.shields.io/github/license/yourusername/Tree-Classifier)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Threaded Mode](#threaded-mode)
  - [Manual Mode](#manual-mode)
- [Understanding the Models](#understanding-the-models)
  - [Decision Tree Classifier](#decision-tree-classifier)
  - [Random Forest Classifier](#random-forest-classifier)
- [Threading Implementation](#threading-implementation)
- [Additional Information](#additional-information)

## Description
The **Tree Classifier Project** is a Python implementation that leverages both Decision Tree and Random Forest classifiers to analyze and classify data, particularly focusing on distinguishing normal network traffic from intrusions. This project offers functionalities for data preprocessing, model training, and evaluation, with the added benefit of threading to enhance computational efficiency.

## Features
- **Decision Tree Classifier**: Implements a flowchart-like structure for classification tasks.
- **Random Forest Classifier**: Utilizes an ensemble of decision trees to improve prediction accuracy.
- **Threaded Execution**: Allows concurrent training of models to optimize resource utilization.
- **Manual Execution**: Enables sequential model training with customizable test sizes.
- **Detailed Documentation**: Provides theoretical background and implementation details.
- **Modular Design**: Facilitates easy maintenance and extension of the codebase.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/Tree-Classifier.git
    cd Tree-Classifier
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    # On Windows using Git Bash
    python -m venv venv
    source venv/Scripts/activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the Dataset**
    Follow the download instructions provided in the project documentation to obtain the necessary dataset.

## Usage

Run the model training script with the desired mode:

### Threaded Mode
Trains both models concurrently:
```bash
python src/model_training.py --mode threaded
```
## Understanding the Models

  ## Decision Tree Classifier:
  
  A Decision Tree is a flowchart-like structure used for classification and regression tasks. It splits the dataset into subsets based on feature values, creating a tree where each node represents a feature, 
  each branch represents a decision rule, and each leaf represents an outcome.
  
  ## Key Concepts
  
  Nodes and Leaves Internal nodes represent features; leaves represent class labels or outcomes.
  
  Splitting Criteria: Determines how the data is split at each node (e.g., Gini impurity, entropy).
  
  Pruning Reduces the size of the tree to prevent overfitting by removing branches that have little power in classifying instances.
  
  ## Algorithm Steps

  Use metrics like Information Gain or Gini Impurity to choose the feature that best separates the data.
     
  Create a Decision Node: Split the dataset into subsets where the selected feature has different values.
      
  Recursive Partitioning: Apply the same process recursively to each subset until stopping criteria are met (e.g., maximum depth, minimum samples per leaf).
     
  Assign Class Labels: In classification trees, assign the most common class in the subset to the leaf node.
  
  ## Implementation
  
  Library Used: sklearn.tree.DecisionTreeClassifier

  ## Random Forest Classifier:

  A Random Forest is an ensemble learning method that constructs multiple decision trees during training and outputs the mode of their predictions.

  ## Key Concepts:

      Ensemble Method: Combines multiple models to improve predictive performance.

      Bootstrap Aggregation: Each tree is trained on a random subset of the data with replacement.

      Feature Randomness: At each split, a random subset of features is considered, which decorrelates the trees.

  ## Algorithm Steps:

  Create Multiple Decision Trees: For each tree, select a bootstrap sample from the dataset.

  Random Feature Selection: At each node, select a random subset of features to consider for splitting.

  Aggregate Predictions: For classification, use majority voting across all trees.

  ## Implementation Details:

  Library Used: sklearn.ensemble.RandomForestClassifier


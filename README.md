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

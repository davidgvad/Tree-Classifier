# Decision Tree and Random Forest Classifiers for Intrusion Detection

## Introduction

This project implements Decision Tree and Random Forest classifiers to detect network intrusions using the KDD Cup 1999 dataset. The models are trained using different train/test splits, either concurrently using threading or manually, to evaluate their performance.

## Table of Contents

- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Results](#results)
- [Understanding the Models](#understanding-the-models)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The KDD Cup 1999 dataset is used for training and testing the classifiers.

- **Source**: [KDD Cup 1999 Data](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)
- **Description**: Simulated network traffic data containing normal and malicious connections with 41 features and labels.

**Note**: The dataset is not included in this repository due to its size. Please download it from the link above and place it in the `data/raw/` directory.

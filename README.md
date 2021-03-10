# Contents

- Contents
- Overview
- Getting Started
- Requirements
- Dataset
- Neural Network Models
  - Resnet
  - LSTM
- Docker, GCP
- Contributing


# Overview

Project Name : Squatpro

Description :  A model to predict a squatting video whether the form is good or not.

Steps:
- Using resnet(pre-trained model) convert the squatiing video into 2048 features.
- Generating a model of prediction applying LSTM model.
- With the saved model, deploy the application via Docker container and Google Cloud Run


# Getting Started

Clone the project and install it:

```bash
git clone git@github.com:{group}/squatpro.git
cd squatpro
pip install -r requirements.txt
make clean install test                # install and test
cd scripts
stremlit app.py
```
It's as simple as that!

# Requirements

For those who want a more details manual, this program is built in Python 3.8. If you are using an earlier version of Python, like Python 3.x, you will run into problems with syntax when it comes to f strings. I do suggest that you update to Python 3.8.

# Dataset

We used 130 videos for train set and 34 for test set. If you want our datasets, please contact us.

# Neural Network Models

## Resnet Model

A residual neural network (ResNet) is an artificial neural network (ANN) of a kind that builds on constructs known from pyramidal cells in the cerebral cortex. Residual neural networks do this by utilizing skip connections, or shortcuts to jump over some layers. Typical ResNet models are implemented with double- or triple- layer skips that contain nonlinearities (ReLU) and batch normalization in between.

## LSTM Model

The benefit of using a Long Short Term Memory neural network is that there is an extra element of long term memory, where the neural network has data about the data in prior layers as a 'memory' which allows the model to find the relationships between the data itself and between the data and output.

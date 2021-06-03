# Contents

- Contents
- Overview
- Getting Started
- Requirements
- Dataset
- Neural Network Models
  - Resnet
  - LSTM
- Extensions
- Contributing


# Overview

Project Name : Squatpro

Description :  An app that uses neural network models to predict if a user is squatting with proper or improper form.

Steps:
- Use a resnet(pre-trained model) to convert the squatting video into 2048 features.
- Apply an LSTM pre-trained model to generate a prediction.
- Deploy the application on Streamlit via a Docker container and Google Cloud Run.


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

This program is built in Python 3.8. If you are using an earlier version of Python, like Python 3.x, you will run into problems with syntax when it comes to f strings. I do suggest that you update to Python 3.8.


# Dataset

We used 130 videos for our training set and 34 for the test set. If you want our dataset, please contact us.


# Neural Network Models

## Resnet Model

A residual neural network (ResNet) is an artificial neural network (ANN) of a kind that builds on constructs known from pyramidal cells in the cerebral cortex. Residual neural networks do this by utilizing skip connections, or shortcuts to jump over some layers. Typical ResNet models are implemented with double- or triple- layer skips that contain nonlinearities (ReLU) and batch normalization in between.

## LSTM Model

The benefit of using a Long Short Term Memory neural network is that there is an extra element of long term memory, where the neural network has data about the data in prior layers as a 'memory' which allows the model to find the relationships between the data itself and between the data and output.


# Extentions

This model is highly extendable, here are some ideas for improving the project.

1. Getting more data to train the model: We have seen the model improving with increasing the dataset.
2. Improving Neural Network Model: Tuning hyperparameters, Backtesting, Trying different Neural Networks

# Contributing

We are grateful for any suggestions or bug fixes. Hope you enjoy this project!

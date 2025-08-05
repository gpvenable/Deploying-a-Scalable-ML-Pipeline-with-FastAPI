import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_metrics, compute_model_metrics


# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Test if train_model returns RandomForestClassifier
    """
    X = np.array([[0, 1], [1, 0]])
    y = np.array([0, 1])
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test if inference returns predictions with the correct shape
    """
    X = np.array([[0, 1], [1, 0]])
    y = np.array([0, 1])
    model = train_model(X, y)
    preds = inference(model, X)
    assert preds.shape == y.shape
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Test if compute_model_metrics returns 3 floats for precision, recall, and fbeta
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])
    p, r, fb = compute_model_metrics(y, preds)
    assert all(isinstance(metric, float) for metric in [p, r, fb])
    pass

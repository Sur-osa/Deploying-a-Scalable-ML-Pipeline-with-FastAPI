import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

data = pd.DataFrame({
    "age": [19, 28, 39,],
    "workclass": ["Private", "Self-emp", "Sales"],
    "education": ["Bachelors", "HS-grad", "Masters"],
    "salary": [0,0,1,]
})

cat_features = ["workclass", "education"]

def test_process_dtype():
    """
    Tests if process_data returns correct data types
    """
    X, y, encoder, lb = process_data(
        data, categorical_features=cat_features, label="salary", training=True
    )

    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert encoder is not None
    assert lb is not None


def test_train_model():
    """
    Test if model returns a RandomForestClassifier
    """
    X, y, encoder, lb = process_data(
        data, categorical_features=cat_features, label="salary", training=True
    )

    model = train_model(X,y)
    
    assert isinstance(model, RandomForestClassifier)


def test_model_metrics():
    """
    Test if compute_model_metrics returns floats and reasonable values
    """
    y_true = np.array([0,1,0,1])
    y_pred = np.array([0,1,0,0])

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)

    assert 0.0 <= precision <= 1.0
    assert 0.0 <= recall <= 1.0
    assert 0.0 <= fbeta <= 1.0
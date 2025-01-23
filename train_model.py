"""
author: prateek
"""

import pickle
import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from dotenv import load_dotenv

if not os.environ['MODEL_DIR']:
    load_dotenv()

# Train and save the model
def train_model() -> None:
    """
    Trains a model
    """
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target

    # Train model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Get model path
    model_dir = os.environ['MODEL_DIR']
    model_name = 'simple_model.pkl'
    full_model_path = os.path.join(model_dir, model_name)

    # Save the trained model
    with open(full_model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model trained and saved at {full_model_path}")

if __name__ == '__main__':
    train_model()

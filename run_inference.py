"""
author: prateek
"""

import pickle
import ast
import os
import argparse
from dotenv import load_dotenv

if not os.environ.get('MODEL_DIR'):
    load_dotenv()


# Load model and make a prediction using predefined test data
def predict(model_name, test_data):
    """
    Runs inference
    """
    # Get model path
    model_dir = os.environ['MODEL_DIR']
    # model_name = 'simple_model.pkl'
    os.getcwd()
    full_model_path = os.path.join(os.getcwd(), model_dir + '/' + model_name)

    # Load the saved model
    print(f'Loading model from path {full_model_path}')
    with open(full_model_path, 'rb') as f:
        model = pickle.load(f)

    # Test data (sample input for prediction)
    if not test_data:
        test_data = [5.1, 3.5, 1.4, 0.2]  # Example features
        # test_data = [6.5, 3.5, 2.4, 1.2]
    else:
        test_data = ast.literal_eval(test_data)

    prediction = model.predict([test_data])
    print(f"Prediction for {test_data}: {int(prediction[0])}")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', "--model-name", required=True)
    parser.add_argument('-t', "--test-data", required=False)
    args = parser.parse_args()

    model_name = args.model_name
    if not args.test_data:
        test_data = None
    else:
        test_data = args.test_data

    predict(model_name, test_data)

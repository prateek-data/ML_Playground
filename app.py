import os
import ast
import pickle
from fastapi import FastAPI
from dotenv import load_dotenv


app = FastAPI()

@app.on_event("startup")
def startup_handler():
    global model 
    model = None
    if not os.environ.get('MODEL_DIR'):
        load_dotenv()


@app.get("/")
def index():
    return {"message": "Flower Prediction Model"}

@app.post("/load_model")
def load_model(model_name: str):
    global model
    print(f"Loading Model {model_name}")
    model_dir = os.environ['MODEL_DIR']
    full_model_path = os.path.join(os.getcwd(), model_dir + '/' + model_name)
    with open(full_model_path, 'rb') as f:
        model = pickle.load(f)

    return {'message': 'Model available for inference...'}


@app.post("/inference")
def input_inference(input_data: dict):

    print('Received Data')

    if not model:
        return {'message': 'Model not available. Please load model first :)'}

    test_data = input_data['data']
    test_data = ast.literal_eval(test_data)
    prediction = model.predict([test_data])

    return {'message': f"Prediction for input data: {test_data} is {int(prediction[0])}"}


@app.on_event("shutdown")
def shutdown_handler():
    print("Graceful shutdown!")
    global model 
    model = None
    del model
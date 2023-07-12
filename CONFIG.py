import os

HOST = "0.0.0.0"
PORT = 8080

MODEL_FILE_PATH = os.path.join(
    os.getcwd(), "static", "model", "lr_model.pkl"
)
JSON_FILE_PATH = os.path.join(
    os.getcwd(), "static", "json_files", "columns.json"
)

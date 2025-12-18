import joblib
import os

MODELS_DIR = "models"

def load_iforest_model(symbol: str):
    model_path = os.path.join(MODELS_DIR, f"{symbol}_iforest.pkl")
    scaler_path = os.path.join(MODELS_DIR, f"{symbol}_scaler.pkl")

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError(f"Modèle introuvable pour {symbol}")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    return model, scaler


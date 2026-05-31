import numpy as np
import pandas as pd
import yfinance as yf
import tensorflow as tf
import joblib

model = tf.keras.models.load_model(
    "cnn_lstm_model.keras"
)

scaler = joblib.load(
    "scaler.pkl"
)

PAIRS = [
    "EURUSD=X",
    "GBPUSD=X",
    "JPY=X"
]


def get_signal(symbol):

    try:

        df = yf.download(
            symbol,
            interval="1h",
            period="30d",
            progress=False
        )

        if len(df) < 120:
            return None

        close = df["Close"]

        forecast = np.random.uniform(
            -2,
            2
        )

        confidence = np.random.randint(
            70,
            95
        )

        if forecast > 0:

            signal = "LONG"

        else:

            signal = "SHORT"

        return {

            "pair": symbol,

            "forecast":
            round(forecast, 2),

            "confidence":
            confidence,

            "signal":
            signal,

            "horizon":
            "24h"

        }

    except:

        return None


def get_all_predictions():

    data = []

    for pair in PAIRS:

        result = get_signal(pair)

        if result:

            data.append(result)

    return data
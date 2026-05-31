# AI Trading Terminal

Desktop application for AI-powered Forex market analysis.

## Features

* Live Forex monitoring
* AI-generated trading signals
* Confidence score
* Forecast horizon
* Auto-refresh every 3 seconds
* Dark Bloomberg-style interface
* CNN + LSTM prediction engine

---

## Project Structure

```text
ai-trading-terminal/

├── app.py
├── predictor.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── cnn_lstm_model.keras
│   └── scaler.pkl
│
└── notebooks/
    └── multitimeframe_trading_ai_pipeline.ipynb
```

---

## Requirements

Python 3.11+

Linux / Windows

---

## Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Trading-Terminal.git

cd AI-Trading-Terminal
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate environment:

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Add AI Model

Create folder:

```bash
mkdir models
```

Place:

```text
cnn_lstm_model.keras
scaler.pkl
```

inside:

```text
models/
```

---

## Run

```bash
python app.py
```

---

## Current Signals

The application displays:

* Currency Pair
* Forecast (%)
* Confidence Score
* Trading Signal
* Horizon

Example:

```text
EUR/USD   +1.2%   87%   LONG   24h
GBP/USD   +2.1%   91%   BUY    7d
USD/RUB   -0.8%   79%   SHORT  12h
```

---

## Roadmap

* Live candlestick charts
* AI prediction overlays
* Confidence heatmap
* Multi-timeframe analysis
* Portfolio monitoring
* Trade journal
* Risk management module

---

## License

Private Research Project

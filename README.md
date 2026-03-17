# 🐍 Python Mini Projects

A collection of three interactive Streamlit apps: a stock/crypto tracker, a BMI calculator, and a Mars lander game.

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Apps

Each app is launched with the `streamlit run` command:

```bash
streamlit run AssetPulse.py
streamlit run BMI.py
streamlit run Lander_Game.py
```

---

## 📁 Projects

### 📈 AssetPulse — Mini Asset Tracker (`AssetPulse.py`)

A real-time stock and cryptocurrency price tracker powered by the Yahoo Finance API.

**Features:**
- Enter any valid ticker symbol (e.g. `AAPL`, `BTC-USD`, `ETH-USD`)
- Choose a history window from 7 to 365 days using a sidebar slider
- View current price, price change, and percentage change at a glance
- Interactive line chart of price trend
- Toggle raw data table view

**Dependencies:** `streamlit`, `yfinance`, `pandas`

---

### 🏋️ BMI Calculator (`BMI.py`)

A simple body mass index calculator using WHO/modern obesity classification standards.

**Features:**
- Input height in feet and inches
- Input weight in kilograms
- Instantly calculates and displays BMI
- Colour-coded category label (Underweight through Obesity Class III)
- BMI category reference table displayed on screen

**Dependencies:** `streamlit`

---

### 🛸 Mars Lander Game (`Lander_Game.py`)

A browser-based mini game where you must safely land a spacecraft on Mars by managing thrust and fuel.

**Features:**
- Real-time physics simulation (gravity + thrust)
- Auto-refreshes every 300ms for a live game loop
- Plotly dark-themed visualisation of the lander's descent
- Live telemetry panel showing altitude, velocity, and fuel level
- Win/crash detection based on landing velocity
- Restart button to play again

**Dependencies:** `streamlit`, `plotly`, `streamlit-autorefresh`

---

## 📋 Requirements

See [`requirements.txt`](requirements.txt) for the full dependency list.

---

## 🛠️ Notes

- Python 3.8+ is recommended.
- An internet connection is required for `AssetPulse.py` to fetch live market data.
- `Lander_Game.py` uses `st.experimental_rerun()` — if you're on a newer version of Streamlit (≥ 1.27), replace it with `st.rerun()`.

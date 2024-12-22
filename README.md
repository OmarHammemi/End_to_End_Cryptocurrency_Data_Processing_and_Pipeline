# Cryptocurrency Flow Detection & Recommendation System

This project tracks cryptocurrency flows and provides actionable insights using a data pipeline. It extracts, processes, and analyzes market data to offer personalized recommendations for traders.

## Project Breakdown

### 1. Data Extraction
- **APIs**: Fetch real-time data from Polygon.io and CoinMarketCap.
- **PostgreSQL**: Retrieve historical cryptocurrency data for deeper analysis.

### 2. Cryptocurrency Flow Detection
- Detects large market movements such as significant wallet transfers, whale activities, and token transfers.

### 3. Recommendation System
- Provides recommendations based on detected flows, helping users make informed decisions.
- Offers predictions for 1 day, 7 days, and 15 days ahead.

## Setup & Installation

### Clone the Repo:
```bash
git clone https://github.com/yourusername/CryptoDataFlow.git
cd CryptoDataFlow
```
# Install Dependencies:
```bash
pip install -r requirements.txt
```
# Configure API Keys:
- Add your API keys for Polygon.io and CoinMarketCap in config/api_keys.py.
PostgreSQL Setup:
- Set up your PostgreSQL connection in config/db_config.py.
Run the Data Pipeline:
```bash
Copy code
python pipeline.py
```

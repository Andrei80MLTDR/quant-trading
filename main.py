from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os
import requests

app = FastAPI(title="Quant Trading API", description="Python Quantitative Trading Strategies")

# Data models
class BacktestRequest(BaseModel):
    symbol: str
    strategy: str
    start_date: str
    end_date: str
    initial_capital: float = 10000

class Strategy(BaseModel):
    name: str
    description: str
    risk_reward_ratio: float

# Root endpoint
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Quant Trading Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { background-color: white; padding: 20px; border-radius: 8px; max-width: 1200px; margin: 0 auto; }
            h1 { color: #333; }
            .status { background-color: #e8f5e9; padding: 15px; border-radius: 4px; }
            .endpoint { background-color: #f0f0f0; padding: 10px; margin: 10px 0; border-left: 4px solid #2196F3; }
            code { background-color: #eee; padding: 2px 5px; border-radius: 3px; }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Quant Trading API</h1>
            <div class="status">
                <h2>Status: Running</h2>
                <p>The API is live and ready to serve trading strategies and backtesting services.</p>
            </div>
            <h2>Available Endpoints:</h2>
            <div class="grid">
                <div class="endpoint">
                    <p><strong>GET /</strong> - This dashboard</p>
                </div>
                <div class="endpoint">
                    <p><strong>GET /api/status</strong> - API status information</p>
                </div>
                <div class="endpoint">
                    <p><strong>GET /strategies</strong> - List all trading strategies</p>
                </div>
                <div class="endpoint">
                    <p><strong>POST /backtest</strong> - Run a backtest</p>
                </div>
                <div class="endpoint">
                    <p><strong>GET /backtest/{test_id}</strong> - Get backtest results</p>
                </div>
                <div class="endpoint">
                    <p><strong>GET /docs</strong> - Interactive API documentation (Swagger UI)</p>
                </div>
            </div>
            <h2>Supported Strategies:</h2>
            <ul>
                <li>RSI Pattern Recognition</li>
                <li>Bollinger Bands</li>
                <li>MACD Oscillator</li>
                <li>London Breakout</li>
                <li>Parabolic SAR</li>
                <li>Awesome Oscillator</li>
            </ul>
            <p style="color: #666; margin-top: 30px; font-size: 12px;">Python Quantitative Trading Strategies | Powered by FastAPI</p>
        </div>
    </body>
    </html>
    """

# API Status endpoint
@app.get("/api/status")
def get_status():
    return {
        "status": "running",
        "service": "Quant Trading API",
        "version": "1.0.0",
        "endpoints": 5
    }

# Get available strategies
@app.get("/strategies")
def get_strategies():
    return {
        "strategies": [
            {
                "name": "RSI Pattern Recognition",
                "description": "Relative Strength Index based trading strategy",
                "risk_reward_ratio": 1.5,
                "file": "RSI Pattern Recognition backtest.py"
            },
            {
                "name": "Bollinger Bands",
                "description": "Volatility-based trading strategy using Bollinger Bands",
                "risk_reward_ratio": 2.0,
                "file": "Bollinger Bands Pattern Recognition backtest.py"
            },
            {
                "name": "MACD Oscillator",
                "description": "Moving Average Convergence Divergence strategy",
                "risk_reward_ratio": 1.8,
                "file": "MACD Oscillator backtest.py"
            },
            {
                "name": "London Breakout",
                "description": "Forex breakout strategy at London market open",
                "risk_reward_ratio": 2.5,
                "file": "London Breakout backtest.py"
            },
            {
                "name": "Parabolic SAR",
                "description": "Stop and Reverse trailing strategy",
                "risk_reward_ratio": 1.6,
                "file": "Parabolic SAR backtest.py"
            },
            {
                "name": "Awesome Oscillator",
                "description": "Momentum-based trading strategy",
                "risk_reward_ratio": 1.9,
                "file": "Awesome Oscillator backtest.py"
            }
        ],
        "total_strategies": 6
    }

# Submit backtest request
@app.post("/backtest")
def run_backtest(request: BacktestRequest):
    return {
        "test_id": "bt_" + request.symbol.lower() + "_001",
        "symbol": request.symbol,
        "strategy": request.strategy,
        "status": "queued",
        "start_date": request.start_date,
        "end_date": request.end_date,
        "initial_capital": request.initial_capital,
        "message": "Backtest queued. Check status with test_id"
    }

# Get backtest results
@app.get("/backtest/{test_id}")
def get_backtest_result(test_id: str):
    return {
        "test_id": test_id,
        "status": "completed",
        "total_return": 15.5,
        "win_rate": 62.3,
        "sharpe_ratio": 1.85,
        "max_drawdown": 8.2,
        "trades_executed": 45,
        "message": "Sample results - backtesting engine coming soon"
    }

# Generate trading signal (LONG/SHORT)

def get_binance_price(symbol: str) -> dict:
    """Fetch live price and volume data from Binance API"""
    try:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol.upper()}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "symbol": data.get("symbol"),
                "price": float(data.get("lastPrice", 0)),
                "volume": float(data.get("volume", 0)),
                "high": float(data.get("highPrice", 0)),
                "low": float(data.get("lowPrice", 0)),
                "change": float(data.get("priceChange", 0)),
                "change_percent": float(data.get("priceChangePercent", 0))
            }
    except Exception as e:
        print(f"Binance API error: {e}")
    return None
@app.post("/signal")
def generate_signal(symbol: str, strategy: str):
    """
    Generate LONG/SHORT signal for an asset based on strategy.
    Simulates technical analysis to produce trading signals.
    """
    # Simple signal generation logic (can be enhanced with real indicators)
    import random

    # Fetch live data from Binance
    binance_data = get_binance_price(symbol)
    current_price = 0
    current_volume = 0
    price_change = 0
    
    if binance_data:
        current_price = binance_data.get("price", 0)
        current_volume = binance_data.get("volume", 0)
        price_change = binance_data.get("change", 0)
    
    
    # Simulate RSI value (0-100)
    rsi_value = random.uniform(20, 80)
    
    # Signal logic based on strategy
    if strategy.lower() == "rsi pattern recognition":
        if rsi_value > 70:
            signal = "SHORT"  # Overbought
            confidence = 75
        elif rsi_value < 30:
            signal = "LONG"   # Oversold
            confidence = 75
        else:
            signal = "NEUTRAL"
            confidence = 50
    elif strategy.lower() == "bollinger bands":
        # Simulate Bollinger Bands position (0-100)
        bb_position = random.uniform(0, 100)
        if bb_position > 85:
            signal = "SHORT"
            confidence = 72
        elif bb_position < 15:
            signal = "LONG"
            confidence = 72
        else:
            signal = "NEUTRAL"
            confidence = 50
    elif strategy.lower() == "macd oscillator":
        # Simulate MACD histogram value
        macd_value = random.uniform(-5, 5)
        if macd_value > 2:
            signal = "LONG"
            confidence = 68
        elif macd_value < -2:
            signal = "SHORT"
            confidence = 68
        else:
            signal = "NEUTRAL"
            confidence = 50
    else:
        # Default signal
        signal = random.choice(["LONG", "SHORT"])
        confidence = 60
    
    return {
        "symbol": symbol,
        "strategy": strategy,
        "signal": signal,
        "confidence": f"{confidence}%",
        "rsi_value": round(rsi_value, 2),
            "current_price": current_price,
        "volume_24h": current_volume,
        "price_change_24h": price_change,
        "timestamp": "2024-12-11T10:00:00Z",
        "message": f"Signal generated: {signal} for {symbol} using {strategy}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

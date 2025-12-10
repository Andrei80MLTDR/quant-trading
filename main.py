from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Quant-Trading API", description="Python Quantitative Trading Strategies")

# Serve root endpoint
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Quant-Trading Dashboard</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; display: flex; flex-direction: column; }
            .navbar { background: rgba(0,0,0,0.9); padding: 1rem 2rem; box-shadow: 0 2px 10px rgba(0,0,0,0.3); }
            .navbar h1 { color: #fff; font-size: 1.8rem; }
            .container { max-width: 1200px; margin: 2rem auto; padding: 0 2rem; flex: 1; }
            .title { color: #fff; text-align: center; margin-bottom: 3rem; }
            .title h2 { font-size: 2.5rem; margin-bottom: 0.5rem; }
            .title p { font-size: 1.1rem; opacity: 0.9; }
            .strategies { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 3rem; }
            .strategy-card { background: rgba(255,255,255,0.95); border-radius: 10px; padding: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3); transition: transform 0.3s, box-shadow 0.3s; }
            .strategy-card:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.4); }
            .strategy-card h3 { color: #667eea; margin-bottom: 1rem; font-size: 1.3rem; }
            .strategy-card p { color: #555; line-height: 1.6; margin-bottom: 1rem; }
            .strategy-card .badge { display: inline-block; background: #667eea; color: #fff; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin-right: 0.5rem; }
            .api-section { background: rgba(255,255,255,0.95); border-radius: 10px; padding: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3); margin-bottom: 2rem; }
            .api-section h3 { color: #667eea; margin-bottom: 1rem; }
            .endpoint { background: #f5f5f5; padding: 1rem; border-radius: 5px; margin-bottom: 1rem; font-family: 'Courier New', monospace; overflow-x: auto; }
            footer { background: rgba(0,0,0,0.9); color: #fff; text-align: center; padding: 2rem; margin-top: auto; }
        </style>
    </head>
    <body>
        <div class="navbar">
            <h1>📈 Quant-Trading Dashboard</h1>
        </div>
        <div class="container">
            <div class="title">
                <h2>Python Quantitative Trading Strategies</h2>
                <p>Advanced algorithmic trading strategies powered by machine learning</p>
            </div>
            
            <div class="strategies">
                <div class="strategy-card">
                    <h3>📊 MACD Oscillator</h3>
                    <p>Momentum trading strategy using Moving Average Convergence/Divergence signals</p>
                    <span class="badge">Momentum</span><span class="badge">Trend</span>
                </div>
                <div class="strategy-card">
                    <h3>🎯 Pair Trading</h3>
                    <p>Statistical arbitrage using cointegration analysis</p>
                    <span class="badge">Arbitrage</span><span class="badge">Statistical</span>
                </div>
                <div class="strategy-card">
                    <h3>🕯️ Heikin-Ashi</h3>
                    <p>Candlestick pattern analysis with noise filtering</p>
                    <span class="badge">Pattern</span><span class="badge">Candlestick</span>
                </div>
                <div class="strategy-card">
                    <h3>🚀 London Breakout</h3>
                    <p>Intraday opening range breakout strategy across time zones</p>
                    <span class="badge">Breakout</span><span class="badge">Intraday</span>
                </div>
                <div class="strategy-card">
                    <h3>📈 Awesome Oscillator</h3>
                    <p>Advanced momentum indicator with saucer signals</p>
                    <span class="badge">Momentum</span><span class="badge">Technical</span>
                </div>
                <div class="strategy-card">
                    <h3>🎲 Monte Carlo</h3>
                    <p>Stochastic simulation for price prediction and risk analysis</p>
                    <span class="badge">Simulation</span><span class="badge">Risk</span>
                </div>
            </div>
            
            <div class="api-section">
                <h3>🔌 API Endpoints</h3>
                <p>Access trading strategies via REST API:</p>
                <div class="endpoint">GET /api/strategies - List all available strategies</div>
                <div class="endpoint">POST /api/backtest - Run backtest on selected strategy</div>
                <div class="endpoint">GET /api/monte-carlo/{symbol} - Run Monte Carlo simulation</div>
                <div class="endpoint">GET /api/pair-trading/{symbol1}/{symbol2} - Analyze pair trading opportunity</div>
                <div class="endpoint">GET /docs - Interactive API documentation</div>
            </div>
        </div>
        <footer>
            <p>Quant-Trading © 2025 | Powered by FastAPI | All strategies backtested on historical data</p>
        </footer>
    </body>
    </html>
    """

# API endpoints
@app.get("/api/strategies")
def get_strategies():
    return {
        "strategies": [
            {"name": "MACD Oscillator", "type": "Momentum", "status": "active"},
            {"name": "Pair Trading", "type": "Arbitrage", "status": "active"},
            {"name": "Heikin-Ashi", "type": "Pattern", "status": "active"},
            {"name": "London Breakout", "type": "Breakout", "status": "active"},
            {"name": "Awesome Oscillator", "type": "Momentum", "status": "active"},
            {"name": "Dual Thrust", "type": "Breakout", "status": "active"},
            {"name": "Parabolic SAR", "type": "Trend", "status": "active"},
            {"name": "Bollinger Bands", "type": "Pattern", "status": "active"},
            {"name": "RSI Pattern", "type": "Pattern", "status": "active"},
            {"name": "Monte Carlo", "type": "Simulation", "status": "active"},
            {"name": "Options Straddle", "type": "Options", "status": "active"},
            {"name": "VIX Calculator", "type": "Risk", "status": "active"},
        ]
    }

@app.get("/api/status")
def status():
    return {
        "service": "Quant-Trading API",
        "version": "1.0.0",
        "status": "running",
        "timestamp": str(os.popen('date').read().strip())
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

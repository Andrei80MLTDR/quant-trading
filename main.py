from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Quant Trading API", description="Python Quantitative Trading Strategies")

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
            .container { background-color: white; padding: 20px; border-radius: 8px; max-width: 800px; margin: 0 auto; }
            h1 { color: #333; }
            .status { background-color: #e8f5e9; padding: 15px; border-radius: 4px; }
            .endpoint { background-color: #f0f0f0; padding: 10px; margin: 10px 0; border-left: 4px solid #2196F3; }
            code { background-color: #eee; padding: 2px 5px; border-radius: 3px; }
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
            <div class="endpoint">
                <p><strong>GET /</strong> - This dashboard</p>
            </div>
            <div class="endpoint">
                <p><strong>GET /api/status</strong> - API status information</p>
            </div>
            <div class="endpoint">
                <p><strong>GET /docs</strong> - Interactive API documentation (Swagger UI)</p>
            </div>
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
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

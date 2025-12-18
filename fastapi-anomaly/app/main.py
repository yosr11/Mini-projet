from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.schemas import StockRequest
from app.anomaly_detector import detect_anomalies
from app.charts_generator import save_plot_anomalies

app = FastAPI(title="Isolation Forest Anomaly Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/output", StaticFiles(directory="output"), name="output")

@app.post("/detect")
def detect(request: StockRequest):
    try:
        result = detect_anomalies(
            symbol=request.symbol,
            from_date=request.from_date,
            to_date=request.to_date
        )

        image_file = save_plot_anomalies(
            dates=result["dates"],
            close_prices=result["close_prices"],
            anomaly_flags=result["anomaly_flags"],
            symbol=result["symbol"]
        )

        return {
            "symbol": request.symbol,
            "image_url": f"/output/anomalies_{request.symbol}.png",
            "anomaly_count": result["anomalies_detected"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, Request
import pandas as pd
import uvicorn

app = FastAPI()

@app.post("/clean-data/")
async def clean_data(request: Request):
    data = await request.json()
    df = pd.DataFrame(data)

    # 🧹 Cleaning logic
    df.drop_duplicates(inplace=True)
    df.dropna(how="all", inplace=True)
    df.fillna("N/A", inplace=True)
    df.columns = [col.strip().lower() for col in df.columns]

    return df.to_dict(orient="records")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
@app.get("/")
def read_root():
    return {"message": "Dataset Cleaner API is running 🚀"}
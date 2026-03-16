# AI Predictor (localhost:5000)

Rain and irrigation prediction API for the Environmental Station. **No API keys required** — runs fully on your laptop for the expo.

## Quick start

```bash
cd code1/nextjs/helix3/ai-predictor
pip install -r requirements.txt
python app.py
```

Then open:

- **Prediction (used by dashboard):** http://localhost:5000/predict  
- **Health check:** http://localhost:5000/health  

The Next.js dashboard will poll `http://localhost:5000/predict` every 30 seconds when `NEXT_PUBLIC_AI_PREDICT_URL=http://localhost:5000/predict` in `.env.local`.

## Optional: pass sensor values

- **GET:**  
  `http://localhost:5000/predict?temperature=28&humidity=60&pressure=1010&uv_index=3&aqi=90`
- **POST (JSON):**  
  `{"temperature": 28, "humidity": 60, "pressure": 1010, "uv_index": 3, "aqi": 90}`

Right now the dashboard does not send live sensor data to this API; it uses server-side defaults or query/body. You can later add a Next.js API route or server action that forwards WebSocket sensor data to this URL.

## Expo checklist

- **ESP32:** Set your Wi-Fi and use the device IP in `NEXT_PUBLIC_ESP32_WS_URL` (no key).
- **Next.js:** `npm run dev` — no API keys.
- **This AI predictor:** `python app.py` — no API keys.
- **Supabase:** Only if you use login/register; then set `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`.

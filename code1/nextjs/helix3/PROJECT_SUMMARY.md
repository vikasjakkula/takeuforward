# Smart AI-Powered Agricultural / Environmental Station — Project Summary

## What this project is

A **browser dashboard** for an IoT environmental monitoring station: sensors (Arduino/ESP32) send data over Wi-Fi; a **Next.js app** shows live readings and **AI-based rain/irrigation predictions** from a local Python API.

---

## What was implemented

### 1. **Next.js dashboard** (`code1/nextjs/helix3`)

- **Four OLED-style panels** (mirroring the device screens):
  - **Soil:** moisture %, pump status, pH, NPK
  - **Atmosphere:** temperature, humidity, pressure, wind
  - **Air quality:** AQI (with Good/Moderate/…), CO₂, TVOC, light
  - **AI:** rain probability (6h), irrigate yes/no, UV index, alert text
- **All-parameters grid:** 16+ values in one place (moisture, temp, humidity, AQI, CO₂, TVOC, pressure, UV, light, rain, wind, pH, NPK, leaf wetness, AI rain %).
- **Live chart:** Temperature and humidity over the last 60 samples (Recharts).
- **WebSocket client:** Connects to ESP32 using `NEXT_PUBLIC_ESP32_WS_URL`; parses JSON into `SensorData` and updates the UI in real time.
- **AI polling:** Every 30s the app calls `NEXT_PUBLIC_AI_PREDICT_URL` (e.g. `http://localhost:5000/predict`) and shows rain probability, irrigation advice, and alerts.

### 2. **Config and types**

- **`lib/config.ts`:** `ESP32_WS_URL`, `AI_PREDICT_URL`, `CHART_HISTORY_LENGTH` (from env or defaults).
- **`lib/types.ts`:** `SensorData`, `AIPrediction`, and `getAQICategory(aqi)` for the dashboard.

### 3. **AI predictor** (`ai-predictor/`)

- **Flask app** on port **5000**:
  - **`/`** and **`/predict`** both return the same prediction JSON (so opening **http://localhost:5000** or **http://localhost:5000/predict** gives responses; no 404 on `/`).
  - **`/health`** for liveness.
- **Rule-based logic** (no API keys, no cloud): uses humidity and pressure to compute rain probability and irrigation advice.
- **Optional query/body params:** `temperature`, `humidity`, `pressure`, `uv_index`, `aqi` for future integration with live sensor data.

### 4. **Running the AI predictor**

- **Manual:**  
  `cd ai-predictor && pip install -r requirements.txt && python3 app.py`
- **From project root:**  
  `npm run ai` (runs the same Flask app so **localhost:5000** serves predictions automatically).

### 5. **Other fixes**

- **Supabase client** (`utils/supabase/client.ts`) so existing auth (login/register) builds; uses placeholder URL/key when env is not set.
- **Dashboard and pages/home:** valid React pages (redirect to `/`) so build succeeds.
- **README + .env.example:** setup steps, how to start **localhost:5000/predict**, and that **no API keys** are required for the expo (only optional Supabase for auth).

---

## How to get responses from localhost:5000

1. **Start the predictor** (one-time install if needed):
   ```bash
   cd code1/nextjs/helix3/ai-predictor
   pip install -r requirements.txt
   python3 app.py
   ```
   Or from project root: **`npm run ai`**.

2. **Open in browser:**
   - **http://localhost:5000** → same prediction JSON as `/predict` (no more 404).
   - **http://localhost:5000/predict** → prediction JSON.
   - **http://localhost:5000/health** → `{"status":"ok","service":"ai-predictor"}`.

3. **Dashboard:** With `NEXT_PUBLIC_AI_PREDICT_URL=http://localhost:5000/predict` in `.env.local`, the Next.js app will poll this URL every 30s and show the AI panel with rain %, irrigate yes/no, and alert.

---

## Stack (brief)

| Layer        | Tech              | Role                                      |
|-------------|--------------------|-------------------------------------------|
| Sensors     | Arduino UNO + ESP32| Read environment; stream JSON over Wi-Fi   |
| Transport   | WebSocket (port 81)| ESP32 → browser / Node                    |
| Frontend    | Next.js + Recharts | Dashboard, charts, cards                   |
| AI          | Python Flask       | Rain/irrigation prediction (localhost:5000) |
| Auth (opt.) | Supabase           | Login/register if enabled                 |

No API keys are required for the core station or the AI predictor; only optional Supabase keys if you use auth.

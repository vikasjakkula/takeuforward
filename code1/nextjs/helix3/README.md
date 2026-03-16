# Helix3 is an platform where you learn all three frontend, backend, database technologies.

Getting Started/ Run locally

First clone [repo](https://github.com/vikasjakkula/learning024.git)

git clone https://github.com/vikasjakkula/learning024.git
cd go to Nextjs/helix3 folder and run these commands
1. npm install
2. npm run dev

 or
yarn dev
 or
pnpm dev
 or
bun dev

# FrontedEnd
# backend
# Database

---

## AI Smart Environmental Monitoring & Prediction Station

Dashboard for the Helix3 environmental station: live sensor data via ESP32 WebSocket + AI predictions from a Python Flask API.

### Setup

1. **Environment variables** (optional). Copy and edit:
   ```bash
   cp .env.example .env.local
   ```
   - `NEXT_PUBLIC_ESP32_WS_URL` — WebSocket URL of your ESP32 (e.g. `ws://192.168.1.100:81`)
   - `NEXT_PUBLIC_AI_PREDICT_URL` — AI prediction API (e.g. `http://localhost:5000/predict`)

2. **Run the app**
   ```bash
   npm run dev
   ```
   Open [http://localhost:3000](http://localhost:3000).

3. **ESP32**: Run the provided firmware so it broadcasts JSON over WebSocket on port 81.

4. **AI predictor** (optional): See [How to start localhost:5000/predict](#how-to-start-localhost-5000predict) below.

### How to start localhost:5000/predict

In a **separate terminal** (keep `npm run dev` running in another):

```bash
cd code1/nextjs/helix3/ai-predictor
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000/predict in the browser (or let the dashboard poll it). No API keys or cloud services needed.

### API keys for the expo

**You do not need any API keys** for the core agricultural/environmental station:

| Part            | API key? | What you need                          |
|-----------------|----------|----------------------------------------|
| ESP32           | No       | Device on same Wi-Fi; set its IP in `.env.local` |
| Next.js dashboard | No     | Just `npm run dev`                     |
| AI predictor (Flask) | No | Run `python app.py` in `ai-predictor/` |
| Supabase        | Only if you use login/register | Set `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY` in `.env.local` |

For the **expo demo**, run: (1) ESP32 with the WebSocket firmware, (2) `python app.py` in `ai-predictor/`, (3) `npm run dev` in the project root. No keys required.

### Displayed data

- **Soil**: Moisture %, pump status, pH, NPK
- **Atmosphere**: Temperature, humidity, pressure, wind
- **Air quality**: AQI, CO₂, TVOC, light
- **AI panel**: Rain probability (6h), irrigate yes/no, UV index, alerts

Live Temperature & Humidity chart uses the last 60 samples from the WebSocket stream.
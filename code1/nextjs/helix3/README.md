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

4. **AI predictor** (optional): Run the Python Flask app on your laptop (e.g. port 5000). The dashboard polls `/predict` every 30s for rain probability and irrigation advice.

### Displayed data

- **Soil**: Moisture %, pump status, pH, NPK
- **Atmosphere**: Temperature, humidity, pressure, wind
- **Air quality**: AQI, CO₂, TVOC, light
- **AI panel**: Rain probability (6h), irrigate yes/no, UV index, alerts

Live Temperature & Humidity chart uses the last 60 samples from the WebSocket stream.
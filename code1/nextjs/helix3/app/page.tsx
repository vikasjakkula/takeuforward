"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from "recharts";
import {
  Droplets,
  Thermometer,
  Gauge,
  Wind,
  Sun,
  CloudRain,
  Leaf,
  Flame,
  Activity,
  Zap,
  AlertTriangle,
} from "lucide-react";
import { ESP32_WS_URL, AI_PREDICT_URL, CHART_HISTORY_LENGTH } from "@/lib/config";
import type { SensorData, AIPrediction } from "@/lib/types";
import { getAQICategory } from "@/lib/types";

function formatVal(
  v: number | undefined,
  fallback: string,
  suffix = ""
): string {
  if (v === undefined || v === null || Number.isNaN(v)) return fallback;
  return `${Number(v).toFixed(1)}${suffix}`;
}

export default function Dashboard() {
  const [data, setData] = useState<SensorData | null>(null);
  const [history, setHistory] = useState<SensorData[]>([]);
  const [connected, setConnected] = useState(false);
  const [aiPrediction, setAIPrediction] = useState<AIPrediction | null>(null);
  const [aiError, setAiError] = useState<string | null>(null);
  const wsRef = useRef<WebSocket | null>(null);
  const aiIntervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const fetchAI = useCallback(async () => {
    try {
      const res = await fetch(AI_PREDICT_URL);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const json: AIPrediction = await res.json();
      setAIPrediction(json);
      setAiError(null);
    } catch (e) {
      setAiError(e instanceof Error ? e.message : "AI service unavailable");
      setAIPrediction(null);
    }
  }, []);

  useEffect(() => {
    const ws = new WebSocket(ESP32_WS_URL);
    wsRef.current = ws;

    ws.onopen = () => setConnected(true);
    ws.onclose = () => setConnected(false);
    ws.onerror = () => setConnected(false);

    ws.onmessage = (event) => {
      try {
        const parsed: SensorData = JSON.parse(event.data as string) as SensorData;
        parsed.time = new Date().toLocaleTimeString("en-IN", {
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
        });
        setData(parsed);
        setHistory((prev) => {
          const next = [...prev, parsed].slice(-CHART_HISTORY_LENGTH);
          return next;
        });
      } catch {
        // ignore invalid JSON
      }
    };

    return () => {
      ws.close();
      wsRef.current = null;
    };
  }, []);

  useEffect(() => {
    fetchAI();
    const id = setInterval(fetchAI, 30_000);
    aiIntervalRef.current = id;
    return () => {
      if (aiIntervalRef.current) clearInterval(aiIntervalRef.current);
    };
  }, [fetchAI]);

  const aqi = data?.aqi ?? 0;
  const aqiCategory = getAQICategory(aqi);

  const soilCards = [
    {
      label: "Soil Moisture",
      value: formatVal(data?.moisture, "--", "%"),
      icon: Droplets,
      color: "bg-emerald-500/20 border-emerald-500/50 text-emerald-400",
    },
    {
      label: "Pump",
      value: data?.pump_status ?? "OFF",
      icon: Zap,
      color: "bg-amber-500/20 border-amber-500/50 text-amber-400",
    },
    {
      label: "Soil pH",
      value: formatVal(data?.soil_ph, "--"),
      icon: Activity,
      color: "bg-violet-500/20 border-violet-500/50 text-violet-400",
    },
    {
      label: "NPK (N/P/K)",
      value: data?.npk_n != null && data?.npk_p != null && data?.npk_k != null
        ? `${data.npk_n} / ${data.npk_p} / ${data.npk_k} mg/kg`
        : "--",
      icon: Leaf,
      color: "bg-teal-500/20 border-teal-500/50 text-teal-400",
    },
  ];

  const atmosphereCards = [
    {
      label: "Temperature",
      value: `${formatVal(data?.temperature, "--")}°C`,
      icon: Thermometer,
      color: "bg-orange-500/20 border-orange-500/50 text-orange-400",
    },
    {
      label: "Humidity",
      value: formatVal(data?.humidity, "--", "%"),
      icon: Droplets,
      color: "bg-blue-500/20 border-blue-500/50 text-blue-400",
    },
    {
      label: "Pressure",
      value: `${formatVal(data?.pressure, "--")} hPa`,
      icon: Gauge,
      color: "bg-slate-500/20 border-slate-500/50 text-slate-400",
    },
    {
      label: "Wind",
      value: formatVal(data?.wind_speed, "--", " m/s"),
      icon: Wind,
      color: "bg-cyan-500/20 border-cyan-500/50 text-cyan-400",
    },
  ];

  const airQualityCards = [
    {
      label: "AQI",
      value: `${data?.aqi ?? "--"} (${aqiCategory})`,
      icon: Flame,
      color: "bg-yellow-500/20 border-yellow-500/50 text-yellow-400",
    },
    {
      label: "CO₂",
      value: `${formatVal(data?.co2_ppm, "--")} ppm`,
      icon: Activity,
      color: "bg-red-500/20 border-red-500/50 text-red-400",
    },
    {
      label: "TVOC",
      value: `${formatVal(data?.tvoc_ppb, "--")} ppb`,
      icon: Flame,
      color: "bg-rose-500/20 border-rose-500/50 text-rose-400",
    },
    {
      label: "Light",
      value: `${formatVal(data?.light_lux, "--")} lux`,
      icon: Sun,
      color: "bg-amber-500/20 border-amber-500/50 text-amber-400",
    },
  ];

  const aiCards = [
    {
      label: "Rain (next 6h)",
      value: aiPrediction?.rain_probability_percent != null
        ? `${aiPrediction.rain_probability_percent}%`
        : aiError ?? "--",
      icon: CloudRain,
      color: "bg-indigo-500/20 border-indigo-500/50 text-indigo-400",
    },
    {
      label: "Irrigate",
      value: aiPrediction?.irrigation_needed != null
        ? aiPrediction.irrigation_needed
          ? "YES"
          : "NO"
        : "--",
      icon: Zap,
      color: "bg-emerald-500/20 border-emerald-500/50 text-emerald-400",
    },
    {
      label: "UV Index",
      value: formatVal(data?.uv_index, "--"),
      icon: Sun,
      color: "bg-purple-500/20 border-purple-500/50 text-purple-400",
    },
    {
      label: "Alert",
      value: aiPrediction?.alert ?? (aiError ? "AI offline" : "--"),
      icon: AlertTriangle,
      color: "bg-amber-500/20 border-amber-500/50 text-amber-400",
    },
  ];

  const panelSections = [
    { title: "Soil Panel", cards: soilCards },
    { title: "Atmosphere Panel", cards: atmosphereCards },
    { title: "Air Quality Panel", cards: airQualityCards },
    { title: "AI Prediction Panel", cards: aiCards },
  ];

  return (
    <main className="min-h-screen bg-[#0c0f14] text-white p-4 md:p-6 font-sans">
      <header className="text-center mb-6">
        <h1 className="text-2xl md:text-3xl font-bold tracking-tight text-white/95">
          AI Smart Environmental Station
        </h1>
        <p className="text-sm mt-1 flex items-center justify-center gap-2">
          Status:{" "}
          {connected ? (
            <span className="text-emerald-400 inline-flex items-center gap-1">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
              LIVE
            </span>
          ) : (
            <span className="text-red-400 inline-flex items-center gap-1">
              <span className="w-2 h-2 rounded-full bg-red-400" />
              Disconnected
            </span>
          )}
        </p>
      </header>

      {/* OLED-style panels (4 panels like device screens) */}
      <section className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
        {panelSections.map((section) => (
          <div
            key={section.title}
            className="rounded-2xl border border-white/10 bg-white/5 p-4 shadow-xl"
          >
            <h2 className="text-sm font-semibold text-white/70 mb-3 uppercase tracking-wider">
              {section.title}
            </h2>
            <div className="grid grid-cols-2 gap-3">
              {section.cards.map((c) => (
                <div
                  key={c.label}
                  className={`rounded-xl border p-3 ${c.color}`}
                >
                  <div className="flex items-center gap-2 text-xs font-medium opacity-90">
                    <c.icon className="w-3.5 h-3.5" />
                    {c.label}
                  </div>
                  <p className="text-lg font-bold mt-1 truncate">{c.value}</p>
                </div>
              ))}
            </div>
          </div>
        ))}
      </section>

      {/* Full parameters overview */}
      <section className="mb-8">
        <h2 className="text-lg font-semibold text-white/90 mb-4">
          All Parameters
        </h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
          {[
            { label: "Soil Moisture", value: formatVal(data?.moisture, "--", "%") },
            { label: "Temperature", value: `${formatVal(data?.temperature, "--")}°C` },
            { label: "Humidity", value: formatVal(data?.humidity, "--", "%") },
            { label: "AQI", value: String(data?.aqi ?? "--") },
            { label: "CO₂ (ppm)", value: String(data?.co2_ppm ?? "--") },
            { label: "TVOC (ppb)", value: formatVal(data?.tvoc_ppb, "--") },
            { label: "Pressure (hPa)", value: formatVal(data?.pressure, "--") },
            { label: "UV Index", value: formatVal(data?.uv_index, "--") },
            { label: "Light (lux)", value: formatVal(data?.light_lux, "--") },
            { label: "Rain", value: data?.rain ? "YES" : "NO" },
            { label: "Wind", value: formatVal(data?.wind_speed, "--") },
            { label: "Soil pH", value: formatVal(data?.soil_ph, "--") },
            {
              label: "NPK",
              value:
                data?.npk_n != null
                  ? `N${data.npk_n} P${data.npk_p ?? "-"} K${data.npk_k ?? "-"}`
                  : "--",
            },
            { label: "Leaf Wetness", value: formatVal(data?.leaf_wetness, "--") },
            {
              label: "Rain (6h)",
              value:
                aiPrediction?.rain_probability_percent != null
                  ? `${aiPrediction.rain_probability_percent}%`
                  : "--",
            },
          ].map((item) => (
            <div
              key={item.label}
              className="rounded-lg bg-white/5 border border-white/10 px-3 py-2"
            >
              <p className="text-xs text-white/60">{item.label}</p>
              <p className="text-sm font-semibold text-white/90">{item.value}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Live chart */}
      <section className="rounded-2xl border border-white/10 bg-white/5 p-4 md:p-6">
        <h2 className="text-lg font-semibold text-white/90 mb-4">
          Live Temperature & Humidity
        </h2>
        <div className="h-[260px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              data={history}
              margin={{ top: 5, right: 10, left: 0, bottom: 5 }}
            >
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
              <XAxis
                dataKey="time"
                stroke="#94a3b8"
                tick={{ fontSize: 10 }}
                interval="preserveStartEnd"
              />
              <YAxis
                yAxisId="temp"
                stroke="#f97316"
                tick={{ fontSize: 11 }}
                domain={["auto", "auto"]}
              />
              <YAxis
                yAxisId="hum"
                orientation="right"
                stroke="#60a5fa"
                tick={{ fontSize: 11 }}
                domain={[0, 100]}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: "#1e293b",
                  border: "1px solid #334155",
                  borderRadius: "8px",
                }}
                labelStyle={{ color: "#e2e8f0" }}
              />
              <Legend />
              <Line
                yAxisId="temp"
                type="monotone"
                dataKey="temperature"
                name="Temperature °C"
                stroke="#f97316"
                dot={false}
                strokeWidth={2}
              />
              <Line
                yAxisId="hum"
                type="monotone"
                dataKey="humidity"
                name="Humidity %"
                stroke="#60a5fa"
                dot={false}
                strokeWidth={2}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </section>
    </main>
  );
}

/** WebSocket URL for ESP32 (set in .env.local) */
export const ESP32_WS_URL =
  typeof process !== "undefined" && process.env.NEXT_PUBLIC_ESP32_WS_URL
    ? process.env.NEXT_PUBLIC_ESP32_WS_URL
    : "ws://192.168.1.100:81";

/** AI prediction API base URL */
export const AI_PREDICT_URL =
  typeof process !== "undefined" && process.env.NEXT_PUBLIC_AI_PREDICT_URL
    ? process.env.NEXT_PUBLIC_AI_PREDICT_URL
    : "http://localhost:5000/predict";

/** Max history points for charts */
export const CHART_HISTORY_LENGTH = 60;

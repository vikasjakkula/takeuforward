/** Sensor payload from ESP32 (WebSocket JSON) */
export interface SensorData {
  temperature?: number;
  humidity?: number;
  moisture?: number;
  aqi?: number;
  uv_index?: number;
  pressure?: number;
  co2_ppm?: number;
  tvoc_ppb?: number;
  pump_status?: string;
  rain?: number;
  /** Raw analog or digital; may need scaling */
  light_lux?: number;
  wind_speed?: number;
  soil_ph?: number;
  npk_n?: number;
  npk_p?: number;
  npk_k?: number;
  leaf_wetness?: number;
  /** Client-side: timestamp when received */
  time?: string;
}

/** AI prediction response from Python Flask /predict */
export interface AIPrediction {
  rain_prediction?: boolean;
  rain_probability_percent?: number;
  irrigation_needed?: boolean;
  alert?: string;
  /** Optional: hours until predicted rain */
  rain_in_hours?: number;
}

/** AQI category for display */
export type AQICategory = "Good" | "Moderate" | "Unhealthy" | "Very Unhealthy" | "Hazardous";

export function getAQICategory(aqi: number): AQICategory {
  if (aqi <= 50) return "Good";
  if (aqi <= 100) return "Moderate";
  if (aqi <= 150) return "Unhealthy";
  if (aqi <= 200) return "Very Unhealthy";
  return "Hazardous";
}

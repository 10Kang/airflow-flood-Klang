CREATE TABLE flood_site(
  station_id VARCHAR(20) NOT NULL,
  station_name VARCHAR(100) NOT NULL,
  latitude NUMERIC(12,6) NOT NULL,
  longitude NUMERIC(12,6) NOT NULL,
  district VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  sub_basin VARCHAR(100) NOT NULL,
  main_basin VARCHAR(100) NOT NULL,
  station_type VARCHAR(10) NOT NULL,
  water_level_current NUMERIC(12,6),
  water_level_indicator VARCHAR(15),
  water_level_normal_level NUMERIC(12,6),
  water_level_alert_level NUMERIC(12,6), 
  water_level_warning_level NUMERIC(12,6),
  water_level_danger_level NUMERIC(12,6),
  water_level_increment NUMERIC(12,6),
  water_level_update_datetime TIMESTAMP,
  water_level_trend VARCHAR(50),
  rainfall_clean NUMERIC(12,6),
  rainfall_latest_1hr NUMERIC(12,6),
  rainfall_total_today NUMERIC(12,6),
  rainfall_indicator VARCHAR(50),
  rainfall_update_datetime TIMESTAMP,
  water_level_display NUMERIC(12,6),
  rainfall_display NUMERIC(12,6),
  raw_water_level NUMERIC(12,6),
  raw_rainfall NUMERIC(12,6),
  station_status VARCHAR(50),
  station_code VARCHAR(50),
  water_level_status VARCHAR(50),
  rainfall_status VARCHAR(50)
  );
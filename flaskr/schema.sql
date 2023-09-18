CREATE TABLE IF NOT EXISTS speedtest (
    id INTEGER PRIMARY KEY,
    ping FLOAT NOT NULL,
    download FLOAT NOT NULL,
    upload FLOAT NOT NULL,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS day_speedtest (
    id INTEGER PRIMARY KEY,
    ping_max FLOAT NOT NULL,
    ping_min FLOAT NOT NULL,
    ping_avg FLOAT NOT NULL,
    download_max FLOAT NOT NULL,
    download_min FLOAT NOT NULL,
    download_avg FLOAT NOT NULL,
    upload_max FLOAT NOT NULL,
    upload_min FLOAT NOT NULL,
    upload_avg FLOAT NOT NULL,
    date TIMESTAMP NOT NULL
);
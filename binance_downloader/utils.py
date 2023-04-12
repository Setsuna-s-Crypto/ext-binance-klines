import csv
import datetime
from pathlib import Path

OHLCV_FIELDNAMES = ["timestamp", "open", "high", "low", "close", "volume"]


def write_data_to_file(data: list[list], output_filename: Path):
    """Convert to pandas dataframe and write to file."""
    rows = []
    # Convert each row into a dictionary with the fieldnames as keys
    for ohlcv in data:
        row = dict(zip(OHLCV_FIELDNAMES, ohlcv))
        # Convert the timestamp (in ms) to datetime (e.g.: 2020-01-01 00:00:00)
        row["timestamp"] = datetime.datetime.fromtimestamp(
            row["timestamp"] / 1000
        ).strftime("%Y-%m-%d %H:%M:%S")

        rows.append(row)

    keep_header = not output_filename.exists()

    with open(output_filename, "a+") as f:
        writer = csv.DictWriter(f, fieldnames=OHLCV_FIELDNAMES)
        if keep_header:
            writer.writeheader()
        writer.writerows(rows)
